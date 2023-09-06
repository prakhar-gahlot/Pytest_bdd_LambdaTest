Feature: Video Player

  @LQ-11160
  Scenario: P1_Video Player Tests
  	#Scenario: User see event details after clicking one event review ID
    Given "Reviewer" logs in ARC
    When "Reviewer" filtered out some events in new ARC and the user clicks one event review ID and the user checks the event details above event video
    Then Review ID is displayed correctly and Trigger is displayed correctly and Record Date is displayed based on local time zone and format is YYYY-MM-DD hh:mm AM/PM
    And Vehicle ID is displayed as vehicle name and Vehicle type is displayed correctly and Seatbelt is displayed correctly and Audio is displayed correctly and FPS is displayed correctly

  @LQ-15626
  Scenario: The video controller bar is displayed correctly
    When "Reviewer" opens an event
    Then the video automatically plays with both front and rear camera views and the Rear+Front is selected as default
    And the video controller bar is displayed with backward button, play button, forward button, backward -1 button, forward +1 button, Rear+Front button, Rear button, Front button, Full Screen button, Stopwatch button

  Scenario: the event review page is started at right tab
    When "Reviewer" opens an event
    Then the review page is start at Outcome & Event Trigger tab
