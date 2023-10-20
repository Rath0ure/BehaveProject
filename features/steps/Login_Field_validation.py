from behave import *
from selenium.webdriver.common.by import By
from features.steps.webElements_helper import *

use_step_matcher("re")


@then("verify Email OR Phone is required string on login page")
def EMAIL_OR_PHONE(context):
    context.driver.implicitly_wait(10)
    try:
        text = context.driver.find_element(By.XPATH, obj.Name_is_required).text
    except:
        context.driver.quit()
        assert False, "Test failed"
    if text == "Name is required":
        context.driver.quit()
        assert True, "Test pass"


@then("verify Email Address is required string on login page")
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.Email_address_is_required).text
    except:
        context.driver.quit()
        assert False, "Test failed"
    if text == "Email Address is required":
        context.driver.quit()
        assert True, "Test pass"


@then("verify Phone Number is required string on login page")
def phone_no_is_required(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.Phone_no_is_required).text
    except:
        context.driver.quit()
        assert False, "Test failed"
    if text == "Phone Number is required":
        context.driver.quit()
        assert True, "Test Pass"


@then('verify "Password is required" string on login page')
def password_required(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.password_is_required).text
    except:
        context.driver.quit()
        assert False, "Test failed"
    if text == "Password is required":
        context.driver.quit()
        assert True, "Test pass"


@step("click on login/Sign_up button")
def step_impl(context):
    context.driver.find_element(By.XPATH,obj.signup_signup_button).click()