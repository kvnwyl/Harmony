import os
from utils.ExceptionHandler import ExceptionHandler as ex
from utils.Logging import Logging


class Harmony:
    event_stack = []

    def __init__(self):
        log = Logging()

        for folder in os.listdir("plugins"):
            plugin_path = os.path.join("plugins", folder)
            for file in os.listdir(plugin_path):
                if file.endswith(".py"):
                    file_name = ".".join(file.split(".")[:-1])
                    if file_name.lower() == folder.lower():
                        file_path = os.path.join(plugin_path, file)
                        with open(file_path, "rb") as f:
                            try:
                                exec(compile(f.read(), file_path, 'exec'))
                            except Exception as e:
                                ex.handle_exception(log,
                                                    type(e).__name__,
                                                    "Loading Plugin")

x = Harmony()