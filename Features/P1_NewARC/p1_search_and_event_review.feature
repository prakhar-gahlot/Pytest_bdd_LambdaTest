Feature: Search and Event review

  @LQ-10595
  Scenario: P1_Search and Event review
  #Scenario: Search new event by single Review ID
    Given the user logins to ARC
    When the user input a valid New event Review ID and the user clicks "Filter" button
    Then the related event is filtered out under the New tab and the event count of New tab is shown
    And the event list shows columns: "REVIEW ID","EVENT ID","CREATION DATE","VEHICLE NAME","ER SERIAL"
