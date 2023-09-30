from selene import browser, have


class AlertPage:

    def open(self):
        browser.open('/alerts')
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def click_confirm_button(self):
        browser.element('#confirmButton').click()
        return self

    def check_confirm_alert(self):
        browser.driver.switch_to.alert.accept()
        browser.element('#confirmResult').should(have.text("You selected Ok"))
        return self

    def check_cancel_alert(self):
        browser.driver.switch_to.alert.dismiss()
        browser.element('#confirmResult').should(have.text("You selected Cancel"))
        return self

    def prompt_button_click(self):
        browser.element('#promtButton').click()
        return self

    def input_into_alert(self, text):
        browser.driver.switch_to.alert.send_keys(text)
        browser.driver.switch_to.alert.accept()
        return self

    def assert_input(self, text):
        browser.element('#promptResult').should(have.text(f"You entered {text}"))
        return self
