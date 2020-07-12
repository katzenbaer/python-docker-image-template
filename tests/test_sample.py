from mock import MagicMock, patch, call, ANY, mock_open, sentinel, PropertyMock
from nose_parameterized import parameterized, param
from nose.tools import raises, assert_equal, assert_true, assert_raises
from os.path import join, dirname, abspath
from app_name.app import App

__copyright__ = "Copyright 2020, Terrence Katzenbaer"

__author__ = "Terrence Katzenbaer"
__email__ = "terrence@katzenbaer.me"


class TestApp(object):

    def test_something(self):
        app = App()
        expected_result = True

        actual_result = app.hello_world()

        assert_equal(expected_result, actual_result)
