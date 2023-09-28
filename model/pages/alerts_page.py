from selene import browser, have


class AlertPage:

    def open(self):
        browser.open('/alerts')
        browser.element(".practice-form-wrapper").should(have.text("Alerts"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        return self
