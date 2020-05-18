import requests
import time
from bin.config_handler import Config_Handler


class ReqManager:
    def __init__(self):
        self.url = \
            F"{Config_Handler.url}"
        self.interval = Config_Handler.interval
        pass

    def _check(self):
        a = ""
        try:
            a = requests.get(
                self.url
            ).content.decode('utf-8')
        except requests.exceptions.ConnectionError:
            logging.warning(F"Cannot get <{self.url}>")
        return a

    def wait_for_command(self) -> str:
        while True:
            output = self._check()
            if output:
                return output
            else:
                time.sleep(self.interval)
