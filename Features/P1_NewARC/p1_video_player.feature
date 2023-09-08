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

  @LQ-11159
  Scenario: User still see company info after opening one event video
    When "Reviewer" opens an event
    Then user still sees these info at top of event video: "Lytx ReviewCenter", "Reviewing for: Company A", "Switch Companies" buttons

  @LQ-11698
  Scenario: System loads and automatically plays video clip of event upon the Reviewer landing on page
    When "Reviewer" opens an event by clicking one review ID
    Then both front and rear camera views are shown and the video automatically plays
    And the video height is set to 352 and the video width is set to 1280
    And the following event information is displayed for the corresponding time that is shown on the video: FWD, LAT, TIME, GPS SPEED and the scrubber on the force graph moves along the timeline in sync with the video as it’s playing and the video time is displayed next to the scrubber correctly
