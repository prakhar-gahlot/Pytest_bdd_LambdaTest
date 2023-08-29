Feature: Search and Event review

  @LQ-10595
  Scenario: P1_Search and Event review
  #Scenario: Search new event by single Review ID
    Given the user logins to ARC
    When the user input a valid New event Review ID and the user clicks "Filter" button
    Then the related event is filtered out under the New tab and the event count of New tab is shown
    And the event list shows columns: "REVIEW ID","EVENT ID","CREATION DATE","VEHICLE NAME","ER SERIAL"

  @LQ-10597
  Scenario: Each searched event column is listed correctly in New tab
    When the user filtered a range of Review IDs under New tab
    Then Review ID is displayed and the events in the range are displayed and Event ID is displayed as CustomerString ID
    And Creation Date is event creation date based on local time zone and displayed as format YYYY-MM-DD hh:mm AM/PM
    And Vehicle Name is displayed correctly and ER Serial is displayed correctly
