import json
import os
from utils.ExceptionHandler import ExceptionHandler as ex
from utils.Logging import Logging

class Plugin:
    def __init__(self):
        self.log = Logging()
        self.config=self._load_config()

    def _load_config(self):
        class_name = self.get_instance_name()
        config_path = os.path.abspath("plugins\{0}".format(class_name))

        try:
            with open(os.path.join(config_path, "{0}_config.json".format(class_name))) as f:
                config_dict = json.loads(f.read())
        except Exception as e:
            ex.handle_exception(self.log,
                                type(e).__name__,
                                "{0}_config.json".format(class_name))
            config_dict = {}

        return config_dict

    @classmethod
    def get_instance_name(cls):
        return cls.__name__