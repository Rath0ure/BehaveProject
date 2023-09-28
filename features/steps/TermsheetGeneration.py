import time

from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.steps.RandomMobileOtp import *
from features.steps.webElements_helper import *

use_step_matcher("re")


@step("enter mobile no")
def EnterMobileNo(context):
    mobile_input = context.driver.find_element(By.XPATH, obj.signup_mobile_no_field)
    mobile_number = generate_random_mobile_number()
    mobile_input.send_keys(mobile_number)
    time.sleep(5)


@step("enter password")
def EnterOtp(context):
    context.driver.find_element(By.XPATH, obj.signup_password_field).send_keys("123456")
    time.sleep(5)


@step("enter name")
def Name(context):
    context.driver.find_element(By.XPATH, obj.signup_your_name_field).send_keys("Raghuraj Pratap Singh")
    time.sleep(2)


@step("enter email address")
def step_impl(context):
    context.driver.find_element(By.XPATH, obj.signup_emailAddress_filed).send_keys("Raghuraj+007@velocity.in")


@step("click on sign up button")
def SIGN_UP_BUTTON(context):
    context.driver.find_element(By.XPATH, obj.signup_signup_button).click()
    time.sleep(2)


@step("enter otp for")
def EnterOtp(context):
    context.driver.find_element(By.XPATH, obj.enter_otp_xpath).send_keys("123456")


@step("click on confirm")
def click_on_confirm(context):
    context.driver.find_element(By.XPATH, obj.enter_otp_xpath).click()
