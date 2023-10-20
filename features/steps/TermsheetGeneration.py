import time
from lib2to3.pgen2 import driver

from behave import *
from selenium.common import MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium import webdriver
from features.steps.RandomMobileOtp import *
from features.steps.webElements_helper import *
from SeleniumHelper import SeleniumHelper


@step("enter mobile no")
def EnterMobileNo(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.signup_mobile_no_field)
    context.driver.implicitly_wait(30)
    mobile_input = context.driver.find_element(By.XPATH, obj.signup_mobile_no_field)
    mobile_number = generate_random_mobile_number()
    mobile_input.send_keys(mobile_number)


@step("enter password")
def EnterOtp(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.signup_password_field)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.signup_password_field).send_keys("123456")


@step("enter name")
def Name(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.signup_your_name_field)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.signup_your_name_field).send_keys("Raghuraj Pratap Singh")


@step("enter email address")
def step_impl(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.signup_emailAddress_filed)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.signup_emailAddress_filed).send_keys("Raghuraj+777@velocity.in")


@step("click on sign up button")
def SIGN_UP_BUTTON(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.signup_now_xpath)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.signup_now_xpath).click()


@step("enter otp for")
def EnterOtp(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.enter_otp_xpath)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.enter_otp_xpath).send_keys("123456")


@step("click on confirm")
def click_on_confirm(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.clk_confirm_sign_otp_xpath)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.clk_confirm_sign_otp_xpath).click()


@then("verify get started string")
def get_start(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.get_started_finance_xpath)
    context.driver.implicitly_wait(30)
    try:
        text = context.driver.find_element(By.XPATH, obj.get_started_finance_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "GET STARTED":
        context.driver.close()
        assert True, "Test Passed"


@step('click on Finance')
def click_on_finance(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.get_started_finance_xpath)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.get_started_finance_xpath).click()


@then("verify get started string on card")
def Get_started_card(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.get_started_card_xpath)
    context.driver.implicitly_wait(30)
    try:
        text = context.driver.find_element(By.XPATH, obj.get_started_card_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "GET STARTED":
        context.driver.close()
        assert True, "Test Passed"


@then("verify get started string on payments")
def step_impl(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.get_started_payments_xpath)
    context.driver.implicitly_wait(30)
    try:
        text = context.driver.find_element(By.XPATH, obj.get_started_payments_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "GET STARTED":
        context.driver.close()
        assert True, "Test Passed"


@step("click on get started")
def step_impl(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.get_started_finance_xpath)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.get_started_finance_xpath).click()


@then("verify apply now button get started page")
def apply_now(context):

    SeleniumHelper(context.driver).wait_till_element_is_present(obj.apply_now_xpath)
    context.driver.implicitly_wait(30)
    try:
        text = context.driver.find_element(By.XPATH, obj.apply_now_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Apply Now":
        context.driver.close()
        assert True, "Test Passed"


@step("verify apply now button get started page")
def apply_now(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.apply_now_xpath)
    context.driver.implicitly_wait(30)
    try:
        text = context.driver.find_element(By.XPATH, obj.apply_now_xpath).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Apply Now":
        context.driver.close()
        assert True, "Test Passed"


@step("click on apply now")
def step_impl(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.apply_now_xpath)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.apply_now_xpath)


@then("Verify Business type string on the apply pag")
def Business_type(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.apply_now_xpath)
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, obj.apply_now_xpath).click()
    parent_window = context.driver.current_window_handle
    all_windows = context.driver.window_handles
    for window_handle in all_windows:
        if window_handle != parent_window:
            context.driver.switch_to.window(window_handle)
            try:
                text = context.driver.find_element(By.XPATH, obj.Business_type_xpath).text
                assert text == "Business Type", "Test Failed"
            except:
                context.driver.close()
                assert False, "Test Failed"
            context.driver.close()
            assert True, "Test Passed"


@step("Generate Term-sheet")
def step_impl(context):
    context.driver.implicitly_wait(15)
    context.driver.find_element(By.XPATH, obj.apply_now_xpath).click()
    parent_window = context.driver.current_window_handle
    all_windows = context.driver.window_handles
    for window_handle in all_windows:
        if window_handle != parent_window:
            context.driver.switch_to.window(window_handle)
            context.driver.find_element(By.XPATH, obj.Apparel_and_Footwear_x_path).click()
            time.sleep(5)
            context.driver.find_element(By.XPATH, obj.your_company_name_xpath).send_keys(obj.company_name)
            time.sleep(2)
            context.driver.find_element(By.XPATH, obj.Your_Company_Website_xpath).send_keys(obj.company_web_url)
            time.sleep(2)
            # context.driver.find_element(By.XPATH, obj.your_mobile_no_xpath).send_keys(obj.your_mobile_no)
            mobile_input = context.driver.find_element(By.XPATH, obj.your_mobile_no_xpath)
            mobile_number = generate_random_mobile_number()
            mobile_input.send_keys(mobile_number)

            time.sleep(2)
            context.driver.find_element(By.XPATH, obj.your_email_xpath).send_keys(obj.your_email)
            time.sleep(2)
            context.driver.find_element(By.XPATH, obj.your_name_xpath).send_keys(obj.your_name)

            time.sleep(2)

            context.driver.find_element(By.XPATH, obj.next_xpath).click()
            time.sleep(2)

            context.driver.find_element(By.XPATH, obj.Enter_otp_xpath).send_keys(obj.otp)
            context.driver.find_element(By.XPATH, obj.next_otp_xpath).click()
            time.sleep(2)

            average_online_revenue = context.driver.find_element(By.XPATH, obj.monthly_avg_online_revenue)
            action = ActionChains(context.driver)
            action.drag_and_drop_by_offset(average_online_revenue, 60, 0).perform()
            time.sleep(2)

            gross_margins = context.driver.find_element(By.XPATH, obj.gross_margins_of_your_business)
            action = ActionChains(context.driver)
            action.drag_and_drop_by_offset(gross_margins, 60, 0).perform()
            time.sleep(2)

            # digital_marketing = context.driver.find_element(By.XPATH, obj.digital_marketing_every_month)
            # action = ActionChains(context.driver)
            # action.drag_and_drop_by_offset(digital_marketing, 5, 0).perform()
            # time.sleep(2)

            context.driver.find_element(By.XPATH, obj.slider_next_button_xpath).click()
            time.sleep(2)

            current_cash = context.driver.find_element(By.XPATH, obj.current_cash)
            action = ActionChains(context.driver)
            action.drag_and_drop_by_offset(current_cash, 50, 0).perform()
            time.sleep(2)

            cash_burn = context.driver.find_element(By.XPATH, obj.cash_burn)
            action = ActionChains(context.driver)
            action.drag_and_drop_by_offset(cash_burn, 0, 0).perform()
            time.sleep(2)

            fund_from_velocity = context.driver.find_element(By.XPATH, obj.fund_from_velocity)
            action = ActionChains(context.driver)
            action.drag_and_drop_by_offset(fund_from_velocity, 50, 0).perform()
            time.sleep(2)

            # fund_deploy_in_market = context.driver.find_element(By.XPATH, obj.fund_deploy_in_velocity)
            # action = ActionChains(context.driver)
            # action.drag_and_drop_by_offset(fund_deploy_in_market, 10, 0).perform()
            # time.sleep(2)

            context.driver.find_element(By.XPATH, obj.submit_button_xpath).click()
            time.sleep(35)


@then("verify Term-Sheet Generated")
def TermSheet_Generated(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(obj.Application_Submitted)
    context.driver.implicitly_wait(30)
    try:
        text = context.driver.find_element(By.XPATH, obj.Application_Submitted).text
    except:
        context.driver.quit()
        assert False, "Test Failed"
    if text == "Application Submitted":
        context.driver.quit()
        assert True, "Test Passed"


@step("click on signup button")
def sign_up(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH,obj.signup_signup_button).click()