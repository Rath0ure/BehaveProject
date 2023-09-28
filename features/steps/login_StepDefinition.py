from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.steps.webElements_helper import *


@given("launch web browser")
def launch_web(context):
    context.driver = webdriver.Chrome()


@when("open sign_up_login paqe")
def open_signup_page(context):
    context.driver.get(obj.url)


@then("Verify Sign up no button")
def verify_sign_up_button(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.Sign_up_now_x_path).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "SIGN UP NOW":
        context.driver.close()
        assert True, "Test Passed"


@then("Verify Sign in to continue string on signup_page")
def sign_in_to_string(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.Sign_to_continue).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Sign in to continue":
        context.driver.close()
        assert True, "Test Passed"


@then("verify Enter Email Address OR Phone Number string")
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.Email_phone_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Enter Email Address OR Phone Number":
        context.driver.close()
        assert True, "Test Passed"


@then("verify password string")
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.password_string_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Password":
        context.driver.close()
        assert True, "Test Passed"


@then("verify Remember me string")
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.remind_me_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Remember me":
        context.driver.close()
        assert True, "Test Passed"


@then("verify Forgot password string")
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.remind_me_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Forgot password?":
        context.driver.close()
        assert True, "Test Passed"


@then("verify sign in string")
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.sign_in_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "SIGN IN":
        context.driver.close()
        assert True, "Test Passed"


@then("verify privacy policy string")
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.privacy_policy_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Privacy policy":
        context.driver.close()
        assert True, "Test Passed"
