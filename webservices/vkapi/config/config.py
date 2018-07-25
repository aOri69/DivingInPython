import configparser
import os


class ConfigException(Exception):
    """Base class for exceptions in this module."""
    pass


class OpenException(ConfigException):

    def __init__(self, path: str, message: str) -> None:
        self.path = path
        self.message = message


class ConfigReader:

    def __init__(self, path='config/settings.ini') -> None:
        self.path = path

    def __enter__(self):
        if not os.path.exists(self.path):
            raise OpenException(self.path, '...path not exists...')
        self.config = configparser.ConfigParser()
        self.config.read(self.path)
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            raise exc_type(exc_val)
