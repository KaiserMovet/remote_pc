import logging
import subprocess
import time


class CommandExecutor:

    def __init__(self):
        self._prepare_actions()

    def _prepare_actions(self):
        self.actions = {}
        self.actions["turn_off"] = _ShellInterface.turn_off
        self.actions["logout"] = _ShellInterface.log_out
        self.actions["lock"] = _ShellInterface.lock
        self.actions["screen_off"] = _ShellInterface.screen_off

    def execute(self, cmd):
        fun = self.actions.get(cmd)
        if fun:
            fun(cmd)
        else:
            logging.warning(F"No function for {cmd}")


class _ShellInterface:

    @staticmethod
    def _execute(cmd, ps=True, kill=False):
        if isinstance(cmd, list):
            if ps:
                cmd = "; ".join(cmd)
            else:
                cmd = " || ".join(cmd)
        full_cmd = ""
        if ps:
            full_cmd += "powershell "
        full_cmd += cmd
        logging.info(F"Executing <{full_cmd}>")
        p = subprocess.Popen(full_cmd)
        time.sleep(5)
        p.terminate()

    @classmethod
    def turn_off(cls, cmd=""):
        cls._execute(
           "shutdown /s /c 'Remote_pc: Shutting down computer'")
        logging.info(F"Executing <turn_off> function for {cmd}")

    @classmethod
    def log_out(cls, cmd=""):
        cls._execute(
            "shutdown /l")
        logging.info(F"Executing <log_out> function for {cmd}")

    @classmethod
    def lock(cls, cmd=""):
        cls._execute(
            "rundll32.exe user32.dll,LockWorkStation", False)
        logging.info(F"Executing <log_out> function for {cmd}")

    @classmethod
    def screen_off(cls, cmd=""):
        cmd_command = \
            "(Add-Type '[DllImport(\\\"user32.dll\\\")] public static "\
            "extern int SendMessage(int hWnd, int hMsg, int wParam, "\
            "int lParam); ' -Name a -Pas):: "\
            "SendMessage(-1, 0x0112, 0xF170, 2)"
        cls._execute(
            cmd_command, kill=True)
        logging.info(F"Executing <log_out> function for {cmd}")
