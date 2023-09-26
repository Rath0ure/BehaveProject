import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Objet_Xpath import *


@given('i launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    time.sleep(2)


@when('open velocity login page')
def openVelocityPg(context):
    context.driver.get(obj.url)
    time.sleep(3)


@step('enter username "{user}" and password "{pwd}"')
def EnterUidPass(context, user, pwd):
    context.driver.find_element(By.XPATH, obj.textbox_username_Xpath).send_keys(user)
    context.driver.find_element(By.XPATH, obj.textbox_password_Xpath).send_keys(pwd)
    time.sleep(3)


@step('click on login button')
def ClickLoginButton(context):
    context.driver.find_element(By.XPATH, obj.button_login_Xpath).click()
    time.sleep(5)


@step('enter the "<otp>"')
def EnterOtp(context):
    context.driver.find_element(By.XPATH, obj.Otp_enter).send_keys("123456")
    time.sleep(5)


@step("click on confirm")
def ClkConfirm(context):
    context.driver.find_element(By.XPATH, obj.conirm_otp).click()
    time.sleep(5)


@then("user must login to the dashboard page")
def dashboard(context):
    try:
        text = context.driver.find_element(By.XPATH,
                                          obj.dashboard_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Select the product you want to continue with":
        context.driver.close()
        assert True, "Test Passed"


@step('enter the "{otp}"')
def OtpValidation(context, otp):
    context.driver.find_element(By.XPATH, obj.Otp_enter).send_keys(otp)
    time.sleep(2)


@Then("Verify CHOOSE String on finance section")
def CHOOSE(context):
    try:
        text = context.driver.find_element(By.XPATH,
                                           obj.choose_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "CHOOSE":
        context.driver.close()
        assert True, "Test Passed"
