import requests
import time
from bin.config_handler import Config_Handler


class ReqManager:
    def __init__(self):
        self.url = \
            F"{Config_Handler.url}/{Config_Handler.key}/"\
            F"{Config_Handler.hostname}"
        self.interval = Config_Handler.interval
        pass

    def _check(self):
        a = requests.get(
            self.url
        ).content.decode('utf-8')
        return a

    def wait_for_command(self) -> str:
        while True:
            output = self._check()
            if output:
                return output
            else:
                time.sleep(self.interval)
