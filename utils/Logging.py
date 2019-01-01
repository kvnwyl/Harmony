from datetime import datetime
import json
import os

class Logging:
    def __init__(self):
        self.log_config = {}
        with open("harmony_config.json") as f:
            self.log_config = json.loads(f.read())

        self.debug_level = self.log_config.get("debugLevel", 1)
        self.console_print =  self._parse_bool(self.log_config.get("consolePrint", "false"))

    def debug(self, message):
        if self.debug_level >= 5:
            self._log(message, "DEBUG")

    def warn(self, message):
        if self.debug_level >= 4:
            self._log(message, "INFO")

    def info(self, message):
        if self.debug_level >= 3:
            self._log(message, "WARN")

    def error(self, message):
        if self.debug_level >= 2:
            self._log(message, "ERROR")

    def critical(self, message):
        if self.debug_level >= 1:
            self._log(message, "CRITICAL")

    def _log(self, message, debug_string):
        message = "{0} [{1}] - {2}".format(str(datetime.now()), debug_string, message)
        with open("Harmony.log", "a") as f:
            f.writelines("{0}\r\n".format(message))
        if self.console_print:
            print(message)

    def _parse_bool(self, string_message):
        return string_message.lower() in ["y", "yes", "true"]