import logging
import os
import time

__copyright__ = "Copyright 2020, Terrence Katzenbaer"

__author__ = "Terrence Katzenbaer"
__email__ = "terrence@katzenbaer.me"

log = logging.getLogger(__name__)


class App:
    def __init__(self):
        pass

    def hello_world(self):
        log.info("Hello World!")
        log.info(f"Working directory is {os.getcwd()}")

        log.info(f"Env var test: {os.getenv('SOME_ENV_KEY')}")

        assert(os.getenv('SOME_ENV_KEY') == 'some_env_value')

        time.sleep(1)

        foo = input("What do you want to write? ")

        if not foo:
            log.error("User entered no input.")
            return False

        with open('assets/foo.txt', 'w') as f:
            f.write(foo)

        return True
