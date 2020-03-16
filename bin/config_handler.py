import yaml


class Config_Handler:
    @classmethod
    def load_file(cls, path):
        with open(path, 'r') as file:
            doc = yaml.load(file, Loader=yaml.FullLoader)
        cls.url = doc['url']
        cls.interval = int(doc['interval'])
