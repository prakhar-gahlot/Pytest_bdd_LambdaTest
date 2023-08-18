Feature: Login

  @LQ-9701
  Scenario: P1_NewARC Tests
  # Scenario: The Sign in button will be disabled if only the username is filled in
    Given the login page of New ARC is opened
    When the user only inputs some characters in the username input box
    Then the Sign in button is disabled

  Scenario: The Sign in button will be disabled if only the password is filled in
    When the user only inputs some characters in the password input box
    Then the Sign in button is disabled

  Scenario: The Sign in button will be enabled after filling the username and password
    When the user inputs some characters in the username and password input box
    Then the Sign in button is enabled, the characters in the username are displayed as the entered characters and encrypted characters in the password are displayed as some dots

  Scenario: The Sign in button will be updated to disabled if clear the inputted username and password
    When the user clears the characters in the username and password input box
    Then the Sign in button is disabled

  @LQ-9702
  Scenario: User could not login if the invalid username is filled in
    When the user inputs a invalid username and valid password for reviewer role
    Then the message "Incorrect username or password. Try again." shows below the Password input box

  Scenario: User could not login if the invalid password is filled in
    When the user inputs a valid username and invalid password for reviewer role
    Then the message "Incorrect username or password. Try again." shows below the Password input box

  @LQ-9700
  Scenario: The login page of New ARC is displayed correctly
    Then The title is "Lytx ReviewCenter" displayed with a dark background, Username input box is displayed with watermark "Username", Password input box is displayed with watermark "Password" and "Sign in" button is disabled as default

  @LQ-9704
  Scenario: User could login if the valid username and password is filled in
    When the user inputs valid username and password and the user clicks the Sign in button
    Then the user login successfully, the role and company selection page is opened