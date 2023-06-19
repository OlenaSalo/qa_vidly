from src.pages.login_page import LoginPage


class Application:

    def __init__(self, browser):
        self.browser = browser

    def login_page(self):
        return LoginPage(self.browser)

