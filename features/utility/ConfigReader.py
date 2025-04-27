import configparser
from distutils.command.config import config


class ConfigReader:
    def __init__(self):
        self.path = "features/testdata/config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.path)

    def read(self):
        if self.config is None:
            raise Exception("ConfigReader has not been initialized")
        return self.config