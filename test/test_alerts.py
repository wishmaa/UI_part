import allure
from model.pages.alerts_page import AlertPage

alerts = AlertPage()


@allure.label('owner', 'Roman Sh')
@allure.feature('Alerts page tests')
@allure.title("Alert confirmation")
def test_alert_confirmation():
    with allure.step("Open alert page"):
        alerts.open()
    with allure.step("Click button for trigger alert"):
        alerts.click_confirm_button()
    with allure.step("Click OK, check result"):
        alerts.check_confirm_alert()


@allure.label('owner', 'Roman Sh')
@allure.feature('Alerts page tests')
@allure.title("Alert cancel")
def test_alert_cancel():
    with allure.step("Open alert page"):
        alerts.open()
    with allure.step("Click button for trigger alert"):
        alerts.click_confirm_button()
    with allure.step("Click Cancel, check result"):
        alerts.check_cancel_alert()


@allure.label('owner', 'Roman Sh')
@allure.feature('Alerts page tests')
@allure.title("Check alert prompt box")
def test_alert_prompt_box():
    with allure.step("Open alert page"):
        alerts.open()
    with allure.step("Click prompt button"):
        alerts.prompt_button_click()
    with allure.step("Enter text ino alert"):
        alerts.input_into_alert('input_name')
    with allure.step("Check after input"):
        alerts.assert_input('input_name')
