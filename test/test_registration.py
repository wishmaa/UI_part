import datetime
from model.pages.reg_page import RegPage
from model.users.users import User, UserRequired
import allure

reg_page = RegPage()


@allure.title("Test registration with empty form")
def test_empty_registration_form(setup_browser):
    with allure.step('Open browser'):
        reg_page.open()
    with allure.step('Submit empty form'):
        reg_page.submitting()
    with allure.step('Check highlighting required fields'):
        reg_page.check_required_fields()


@allure.title("Test registration with filling full form")
def test_registration_fill_all_form(setup_browser):
    # Open registration form

    Newreguser = User(
        first_name='petr',
        last_name='Lastname',
        email='testnew@mail.ru',
        gender='Male',
        phone='1234567890',
        birthday=datetime.date(1991, 2, 10),
        subjects='Computer Science',
        hobby='Music',
        image='image.png',
        address='Ulitsa',
        state='NCR',
        city='Delhi'
    )

    with allure.step('Open browser'):
        reg_page.open()
    with allure.step('Fill form'):
        reg_page.fill_all_form(Newreguser)
    with allure.step('Check registration'):
        reg_page.should_have_user_information(Newreguser)


@allure.title("Test registration with filling required fields")
def test_registration_only_required(setup_browser):
    # Open registration form

    user_required_fields = UserRequired(
        first_name='Petr',
        last_name='Lastname',
        gender='Male',
        phone='1234567890'
    )

    with allure.step('Open browser'):
        reg_page.open()
    with allure.step('Fill required fields'):
        reg_page.fill_required_fields(user_required_fields)
    with allure.step('Check registration'):
        reg_page.check_filled_fields(user_required_fields)

