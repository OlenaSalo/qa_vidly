import configparser
import os
import sys

import pytest
from selenium import webdriver
# from selene import Browser, Config
from selene import browser
from webdriver_manager.firefox import GeckoDriverManager


from src.app import Application


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="remote", help="env variable name")


def read_ini():
    config_file = os.environ.get("config-file", "project-config.ini")
    root_path = os.path.join(sys.path[0], config_file)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser


def get_config(request):
    env_name = request.config.getoption("--env")
    try:
        return env_name, read_ini()[env_name]
    except KeyError:
        raise Exception(f"Wrong configuration for env name [{env_name}] NOT present")


def get_driver(env, browser_name):
    if env == "local":
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())

    capabilities = {
        "browserName": browser_name,
        "browserVersion": "",
        "moon:options": {
            "enableVideo": False
        }
    }
    return webdriver.Remote(
        command_executor="http://192.168.64.2:4444/wd/hub",
        desired_capabilities = capabilities)



@pytest.fixture(scope='session')
def set_up_browser(request):
    env_name, app_config = get_config(request)
    browser.config.driver=get_driver(env_name, app_config['browser_name'])
    browser.config.base_url=app_config['base_url']
    browser.config.window_width=int(app_config['window_width'])
    browser.config.window_height=int(app_config['window_height'])

    yield browser
    browser.close()


@pytest.fixture(scope='session')
def app(set_up_browser):
    return Application(set_up_browser)