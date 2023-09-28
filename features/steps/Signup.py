from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from features.steps.webElements_helper import *


@then("verify sign_up_to_continue")
def sign_up_to(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.Sign_up_to_continue_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Sign up to continue":
        context.driver.close()
        assert True, "Test Passed"


@when("open sign_up paqe")
def step_impl(context):
    context.driver.get(obj.stagging_signup_url)


@then("verify your name string on sign_up page")
def YourName(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.your_Name_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Your Name":
        context.driver.close()
        assert True, "Test Passed"


@then("verify email address string on sign_up page")
def emailAddress(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.email_address).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Email Address":
        context.driver.close()
        assert True, "Test Passed"


@then("verify Phone Number string on sign_up page")
def verify_phone_no(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.phone_no_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Phone Number":
        context.driver.close()
        assert True, "Test Passed"


@then("verify I agree to receive updates on WhatsApp string on sign_up page")
def whats_App(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.whatsApp).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "I agree to receive updates on WhatsApp":
        context.driver.close()
        assert True, "Test Passed"


@then("verify Password string on sign_up page")
def passwordString(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.password_signuppage).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Password":
        context.driver.close()
        assert True, "Test Passed"


@then("verify SIGN UP button on sign_up page")
def Sign_up_sign_up(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.signup_signup).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "SIGN UP":
        context.driver.close()
        assert True, "Test Passed"


@then("verify privacy policy button on sign_up page")
def Signup_privacy_policy(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.signup_privacy_policy).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Privacy policy":
        context.driver.close()
        assert True, "Test Passed"


@then("verify sign in now on sign_up page")
def Signup_Sign_in_now(context):
    try:
        text = context.driver.find_element(By.XPATH, obj.signup_sign_in_now).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "SIGN IN NOW":
        context.driver.close()
        assert True, "Test Passed"
