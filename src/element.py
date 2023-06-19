from selene import Config
from selene.core.entity import Element
from selene.core.locator import Locator
from selenium.webdriver.remote.webelement import WebElement


class SeleneElement(Element):


    def __init__(self,  locator: Locator[WebElement]):
        super().__init__(locator)
        # self.element = element