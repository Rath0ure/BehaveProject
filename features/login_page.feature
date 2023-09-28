Feature: Sign_up_login_page

  Scenario: verify SIGN UP NOW button
    Given launch web browser
    When open sign_up_login paqe
    Then Verify Sign up no button



  Scenario: verify Sign in to continue string on signup_page
    Given launch web browser
    When open sign_up_login paqe
    Then Verify Sign in to continue string on signup_page


  Scenario: verify Enter Email Address OR Phone Number string on signup_page
    Given launch web browser
    When open sign_up_login paqe
    Then verify Enter Email Address OR Phone Number string


  Scenario: verify password string on the signup_page
    Given launch web browser
    When open sign_up_login paqe
    Then verify password string


    Scenario: verify Remind me string on the signup_page
    Given launch web browser
    When open sign_up_login paqe
    Then verify Remember me string

    Scenario: verify Forgot password? string on the signup_page
    Given launch web browser
    When open sign_up_login paqe
    Then verify Forgot password string


    Scenario: verify sign in string on the signup_page
    Given launch web browser
    When open sign_up_login paqe
    Then verify sign in string

    Scenario: verify privacy policy string on the signup_page
    Given launch web browser
    When open sign_up_login paqe
    Then verify privacy policy string

