import logging

__copyright__ = "Copyright 2020, Terrence Katzenbaer"

__author__ = "Terrence Katzenbaer"
__email__ = "terrence@katzenbaer.me"

log = logging.getLogger(__name__)


class App:
    def __init__(self):
        pass

    def hello_world(self):
        log.info("Hello World!")
        return True
