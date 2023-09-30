import allure
from model.pages.buttons_page import ButtonsPage

buttons = ButtonsPage()


@allure.title("Test doubleclick button")
def test_doubleclick_button():
    with allure.step("Open buttons page"):
        buttons.open()
    with allure.step("Make doubleclick"):
        buttons.click_on_doubleclick_button()
    with allure.step("Check message after doubleclick"):
        buttons.check_doubleclick_message()


@allure.title("Test right click button")
def test_right_click_button():
    with allure.step("Open buttons page"):
        buttons.open()
    with allure.step("Make right click"):
        buttons.click_on_right_click_button()
    with allure.step("Check message after right click"):
        buttons.check_right_click_message()
