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

  Scenario: The number of searched events is displayed correctly in New tab if search review id range
    When the user input Review ID range and Clicks Filter button in New tab
    Then the result of filtered new events is displayed above event list

  Scenario: The number of searched event is displayed correctly in New tab if search one single review id
    When the user input Review ID and Clicks Filter button in New tab
    Then the result of filtered single event is displayed above event list

  @LQ-11154
  Scenario: The custom behaviors section will not show if there is no enabled custom behaviors
    When the user clicks one reviewID in a group which has no enabled custom behavior and the user opens the Behavior tab and the user clicks "More Behaviors >" button
    Then the Custom Behaviors section is not displayed

  Scenario: Behavior tab’s second page includes the client’s enabled custom behaviors
    When the user clicks one reviewID in a group which has some enabled custom behaviors includes MVAI behaviors and the user opens the Behavior tab and the user clicks "More Behaviors >" button
    Then the Custom Behaviors section is displayed with all enabled custom behaviors and the MVAI custom behaviors are not visible for the "Reviewer" user

  Scenario: The custom behaviors are displayed properly if there are a lot of enabled custom behaviors
    When the user clicks one reviewID in a group which has lots of enabled custom behaviors and the user opens the Behavior tab and the user clicks "More Behaviors >" button
    Then the Custom Behaviors section is displayed with all enabled custom behaviors

  Scenario: The custom behaviors are updated when switch between events in different groups
    When the user clicks one reviewID in a group which has different enabled custom behaviors and the user opens the Behavior tab and the user clicks "More Behaviors >" button
    Then the custom behavior listed in the event is different from the behaviors listed in the previous event

  Scenario: The comments of custom behaviors are displayed correctly
    When the user clicks one reviewID and opens the Behavior tab and the user clicks "More Behaviors >" button and the user checks all custom behaviors and the user clicks "Comments" button
    Then the comments of selected custom behaviors are listed

  Scenario: User could uncheck to cancel the selection of custom behavior
    When the user clicks one reviewID and opens the Behavior tab and the user clicks "More Behaviors >" button and the user checks all custom behaviors and the user uncheck one behavior
    Then the custom behavior is unselected
