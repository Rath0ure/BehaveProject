Feature: Term_sheet login

  Scenario: verify get started on finance
    Given launch web browser
    When open sign_up paqe
    And enter mobile no
    And enter password
    And enter name
    And enter email address
    And click on sign up button
    And enter otp for
    And click on confirm
    Then verify get started string
    #And click on Finance

  Scenario: verify get started on card
    Given launch web browser
    When open sign_up paqe
    And enter mobile no
    And enter password
    And enter name
    And enter email address
    And click on sign up button
    And enter otp for
    And click on confirm
    Then verify get started string on card


  Scenario: verify get started on payments
    Given launch web browser
    When open sign_up paqe
    And enter mobile no
    And enter password
    And enter name
    And enter email address
    And click on sign up button
    And enter otp for
    And click on confirm
    Then verify get started string on payments


  Scenario: verify apply now button
    Given launch web browser
    When open sign_up paqe
    And enter mobile no
    And enter password
    And enter name
    And enter email address
    And click on sign up button
    And enter otp for
    And click on confirm
    And click on get started
    Then verify apply now button get started page


  Scenario: Click on verify now
    Given launch web browser
    When open sign_up paqe
    And enter mobile no
    And enter password
    And enter name
    And enter email address
    And click on sign up button
    And enter otp for
    And click on confirm
    And click on get started
    And verify apply now button get started page
    And click on apply now


  Scenario: Verify Business type string on the apply page
    Given launch web browser
    When open sign_up paqe
    And enter mobile no
    And enter password
    And enter name
    And enter email address
    And click on sign up button
    And enter otp for
    And click on confirm
    And click on get started
    And verify apply now button get started page
    And click on apply now
    Then Verify Business type string on the apply pag

  @sanity
  Scenario: Generate "Term-sheet"
    Given launch web browser
    When open sign_up paqe
    And enter mobile no
    And enter password
    And enter name
    And enter email address
    And click on sign up button
    And enter otp for
    And click on confirm
    And click on get started
    And click on apply now
    And Generate Term-sheet
    Then verify Term-Sheet Generated




