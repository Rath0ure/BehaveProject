Feature: Signup Field Validation

  Scenario: name is required
    Given  launch web browser
    When  open sign_up_login paqe
    And  click on sign up button
    Then verify Email OR Phone is required string on login page

  Scenario: Email Address is required
    Given launch web browser
    When  open sign_up_login paqe
    And click on sign up button
    Then verify Email Address is required string on login page

  Scenario: Phone Number is required
    Given launch web browser
    When  open sign_up_login paqe
    And click on sign up button
    Then verify Phone Number is required string on login page

    Scenario: Password is required
    Given launch web browser
    When  open sign_up_login paqe
    And click on sign up button
    Then verify "Password is required" string on login page
