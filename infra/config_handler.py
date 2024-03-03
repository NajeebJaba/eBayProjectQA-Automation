import os
import json

class ConfigHandler:
    def __init__(self, config_file_name="config.json"):
        current_script_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_script_dir, config_file_name)
        with open(config_path) as config_file:
            self.config = json.load(config_file)
