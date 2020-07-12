import logging

from app_name.app import App

__copyright__ = "Copyright 2020, Terrence Katzenbaer"

__author__ = "Terrence Katzenbaer"
__email__ = "terrence@katzenbaer.me"

log = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    app = App()
    app.hello_world()
