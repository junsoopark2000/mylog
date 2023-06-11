from typing import Union
import yaml


DEFAULT_CONFIG = "./config.yml"  # path/filename


class Config:
    def __init__(self, config_file=DEFAULT_CONFIG):
        self.config = self._read_config(config_file)

    def _read_config(self, config_file: str) -> Union[None, dict]:
        try:
            with open(config_file, "r", encoding="utf-8") as file:
                config = yaml.safe_load(file)
            return config

        except FileNotFoundError as err:
            return None

    def get_config_value(self, section: str, key: str) -> str:
        """get a value in a section"""
        return self.config.get(section, {}).get(key)
