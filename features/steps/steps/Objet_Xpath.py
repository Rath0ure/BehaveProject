class ClassName:
    url = "https://dashboard.stagingvelocity.in/auth/login"
    textbox_username_Xpath = "//input[@placeholder='Email OR Phone']"
    textbox_password_Xpath = "//input[@placeholder='********']"
    button_login_Xpath = "//span[normalize-space()='SIGN IN']"
    Otp_enter = "//input[@placeholder='123456']"
    conirm_otp = "//span[normalize-space()='CONFIRM']"
    dashboard_xpath = "//h3[normalize-space()='Select the product you want to continue with']"
    choose_xpath = "//span[normalize-space()='CHOOSE']"


obj = ClassName()
