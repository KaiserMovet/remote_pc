import yaml
import logging

class Config_Handler:
    @classmethod
    def load_file(cls, path):
        with open(path, 'r') as file:
            doc = yaml.load(file, Loader=yaml.FullLoader)
        cls.url = doc['url']
        cls.interval = int(doc['interval'])
        logging.info(F"CONFIG_HANDLER: Load URL as {cls.url}")
        logging.info(F"CONFIG_HANDLER: Load INTERVAL as {cls.interval}")
