import logging
import sys


class SusunLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        stream_handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        stream_handler.setFormatter(formatter)

        stream_handler.setLevel(logging.INFO)
        self.logger.addHandler(stream_handler)
        self.logger.propagate = False

    def info(self, message):
        self.logger.info("{}".format(message))

    def debug(self, message):
        self.logger.debug("{}".format(message))


susunLogger = SusunLogger("TestLogger")
