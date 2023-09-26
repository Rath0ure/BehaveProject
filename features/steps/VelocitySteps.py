from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('open velocity signup page')
def OpenVelocityPage(context):
    context.driver.get("https://dashboard.stagingvelocity.in/auth/login")


@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH,"//img[@alt='Logo']").is_displayed()
    assert status is True


@then('close browser')
def CloseBrowser(context):
    context.driver.close()
