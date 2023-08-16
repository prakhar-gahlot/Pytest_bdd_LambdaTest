Feature: Login

  @LQ-9700
  Scenario: P1_NewARC Tests
    #Scenario: The login page of New ARC is displayed correctly
    Given the user opens the URL of New ARC
    Then the login page of New ARC is opened. The title is "Lytx ReviewCenter" displayed with a dark background and Username input box is displayed with watermark "Username" and Password input box is displayed with watermark "Password" and "Sign in" button is disabled as default

  @LQ-9704
  Scenario: User could login if the valid username and password is filled in
    When the user inputs valid username and password and the user clicks the Sign in button
    Then the user login successfully, the role and company selection page is opened