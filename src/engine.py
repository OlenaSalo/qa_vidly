from abc import abstractmethod

from selene import Browser, Config

from src.browser import Browser
from src.configuration import Configuration
from src.element import SeleneElement


class Engine:
    @abstractmethod
    def open(self, url):
        raise NotImplementedError


    @abstractmethod
    def element(self, css_xpath_locator: str):
        raise NotImplementedError


class SeleniumEngine(Engine):

     def __init__(self, config: Configuration):
         config = Config(
             driver = config.driver,
             base_url= config.base_url,
             timeout=config.timeout,
             window_width = config.window_width,
             window_height = config.window_height

         )
         self.browser = Browser(config)

     def open(self, url):
         self.browser.open(url)

     def element(self, css_xpath_locator: str):
         return SeleneElement(self.browser.element(css_xpath_locator))

     def close(self):
         return self.browser.close()


