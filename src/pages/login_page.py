import allure

from src.pages.page import Page


class LoginPage(Page):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Open login page")
    def open(self):
        self.browser.open("/admin")

    def login(self):
        self.browser.element("//input[@name='username']").set_value("admin")
        self.browser.element("//input[@name='password']").set_value("123456")
        self.browser.element("//input[@value='Log in']").click()