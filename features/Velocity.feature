Feature: Velocity logo

  Scenario: Logo presence on Velocity signup page
      Given launch chrome browser
      When open velocity signup page
      Then verify that the logo present on page
      And close browser
