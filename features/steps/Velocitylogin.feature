Feature: Velocity login

  Scenario: Login to the Velocity Cx dashboard
    Given i launch chrome browser
    When open velocity login page
    And enter username "6203882311" and password "123456"
    And click on login button
    And enter the "<otp>"
    And click on confirm
    Then user must login to the dashboard page



  Scenario Outline: Login to Velocity with multiple parameters
    Given i launch chrome browser
    When open velocity login page
    And enter username "6203882311" and password "123456"
    And click on login button
    And enter the "<otp>"
    And click on confirm
    Then user must login to the dashboard page
    Examples:
      | otp |
      | 12345|
      | 123456 |
      | 12345 |




