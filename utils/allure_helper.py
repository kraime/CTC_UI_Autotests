import logging

import allure


class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step(message):
            pass

    def emit(self, record):
        self.log(record.getMessage())


class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()

    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)

    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)