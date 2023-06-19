from selene import browser, have


def test_work(app):
    login_page = app.login_page()
    login_page.open()
    login_page.login()

    browser.element("//a[@href='/admin/']").should(have.text("Django administration"))