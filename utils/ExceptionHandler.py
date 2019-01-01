from utils.Logging import Logging

class ExceptionHandler:
    @staticmethod
    def handle_exception(log, exception, sender):
        if exception.lower() == "filenotfounderror":
            log.critical("Could not locate the file: {0}".format(sender))
        if exception.lower() == "jsondecodeerror":
            log.critical(
                ("Unable to decode JSON file: {0}. "
                 "This could be due to invalid "
                 "JSON syntax or an empty file.".format(sender))
                )
        else:
            print("WHOOPS: {0}".format(exception))