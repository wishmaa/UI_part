import time
from os import wait

from selene import browser, have, command


class ButtonsPage:

    def open(self):
        browser.open('/buttons')
        browser.driver.execute_script("$('[id^=google_ads][id$=container__]').remove()")
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def click_on_doubleclick_button(self):
        browser.element('#doubleClickBtn').double_click()
        return self

    def check_doubleclick_message(self):
        browser.element('#doubleClickMessage').should(have.text('You have done a double click'))
        return self

    def click_on_right_click_button(self):
        browser.element('#rightClickBtn').context_click()
        return self

    def check_right_click_message(self):
        browser.element('#rightClickMessage').should(have.text('You have done a right click'))
        return self
