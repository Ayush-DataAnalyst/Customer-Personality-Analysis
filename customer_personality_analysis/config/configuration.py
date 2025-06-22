import os
import yaml

class ConfigurationManager:
    def __init__(self, config_path="config/config.yaml"):
        self.config = self.read_yaml(config_path)

    def read_yaml(self, path_to_yaml):
        with open(path_to_yaml) as yaml_file:
            return yaml.safe_load(yaml_file)
