Feature: Login

  @LQ-9709
  Scenario: ARC_Smoke Tests
  	#Scenario: Reviewer lands on review page after clicking the Select button
    Given the user is in the Login page of New ARC and a user has Reviewer role in some companies
    When the user inputs valid username and password and the user clicks the Sign in button
    And the user select Reviewer role in the Role dropdown list and the user select one company in the company dropdown list and the user clicks the Select button
    Then the Review page is opened

  @LQ-10592
  Scenario: User see selected company after logging in ARC
    When the user logins in ARC with Company A
    Then "Reviewing for: Company A" text is displayed behind "Lytx ReviewerCenter" and "Switch Companies" button with clickable status is displayed behind "Reviewing for: Company A" and there is a Give Feedback link on the top-right corner

  @LQ-10693
  Scenario: Switch to different companies
    When the user clicks "Switch Companies" button and the user selects one Company from dropdown list and clicks "Select" button
    Then the Company is switched successfully

  @LQ-10596
  Scenario: User Search new event by a range of Review IDs
    When the user input a range of Review IDs and Clicks "Filter" button
    Then the filtered Result is displayed under new event list correctly by CreationDate ASC and searched new events are displayed on one page without pagination
    And the value in each column for the new events are displayed correctly

  Scenario: User search returned events by a range of Review IDs
    When the user input a range of Review IDs in the filter under the Returned tab and the user Clicks "Filter" button
    Then the filtered Result is displayed under returned event list correctly by CreationDate ASC and searched returned events are displayed on one page without pagination
    And the value in each column for the returned events are displayed correctly

  @LQ-11162
  Scenario: System loads and automatically plays video clip of event upon the Reviewer landing on page
    When the user clicks one reviewID
    Then the event review page is opened and the both front and rear camera views are shown and the video automatically plays

  Scenario: Select behaviors in opened event review page
    Given the event’s outcome and event trigger are already selected and the user is under "Behaviors" tab
    When the user selects one or more behaviors under "Behaviors" tab
    Then the behaviors are selected with blue check icon

  Scenario: Navigate to "Comments" tab after clicking "Comments" button
    When the user clicks "Comments" button at bottom right
    Then the user is navigated to event's 'Comments' tab

  Scenario: The event is reviewed after clicking "Complete & Next" button
    When the user selects some behaviors and the user clicks "Complete & Next" button in "Comments" tab
    Then the event is disappeared from events list
    And the event status is updated accordingly to F2F in WS and the corresponding task is generated correctly to Due for Coaching task in WS
    And the event score is updated correctly in WS and the behavior/trigger are displayed correctly in WS
