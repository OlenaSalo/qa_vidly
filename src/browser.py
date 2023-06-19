class Browser:
    def __init__(self, engine):
        self.engine = engine

    def open(self, url):
        self.engine.open(url)

    def element(self, css_or_xpath_locator: str):
        return self.engine.element(css_or_xpath_locator)

    def close(self):
        self.engine.close()

