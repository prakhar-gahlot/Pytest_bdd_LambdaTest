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

  @LQ-12479
  Scenario: The force graph could be displayed correctly
    When the user enters the event review page
    Then the X-axis represents time on the force graph and the Y-axis represents force on the force graph
    And the force graph could display correctly for the event same as FWD/LAT/TIME data
    And there is a scrubber shows on the force graph with the video time displayed

  @LQ-11700
  Scenario: User can operate to change the view to Rear view in full-screen mode
    When the user click full-screen button and the user clicks Rear
    Then the video shows the Rear view only in full-screen mode

  Scenario: User can operate to change the view to Front view in full-screen mode
    When the user click full-screen button and the user clicks Front
    Then the video shows the Front view only in full-screen mode

  Scenario: User can exit full-screen mode
    When the user click full-screen button and the user clicks Front and the user clicks Full Screen
    Then the video shows the Front view and exits full-screen mode

  Scenario: User can operate to change the view to Rear+Front view in full-screen mode
    When the user click full-screen button and the user clicks Rear+Front
    Then the video shows the Rear+Front view and exits full-screen mode

  Scenario: User can operate to change the view to Rear view in default mode
    When the user clicks Rear in default mode
    Then the video enter full screen mode and shows the Rear view

  Scenario: User can operate to change the view to Front view in default mode
    When the user clicks Front in default mode
    Then the video enter full screen mode and shows the Front view

  Scenario: User can operate to change the view to Rear+Front view in default mode
    When the user clicks Rear+Front in default mode
    Then the video shows the Rear+Front view in default mode

  Scenario: User can operate to change to full-screen mode and change to Front view
    When the user clicks full-screen button in default mode
    Then the video shows the Front view in full-screen mode

  Scenario: User can click pause button to pause the video
    When the user clicks pause button
    Then the event video is paused

  Scenario: User can click play button to play the video
    When the user clicks play button
    Then the event video plays with correct timeline

  Scenario: User can click backward button to go to the beginning of the video
    When the user clicks backward button
    Then the event video goes to the beginning of the video

  Scenario: User can click forward button to go to the end of the video
    When the user clicks forward button
    Then the event video goes to the end of the video

  Scenario: User can jump to the time point by clicking on force graph
    When the user clicks on force graph
    Then the event video jumps to the time point user clicked

  Scenario: User can jump to the time point by dragging on force graph
    When the user drags on force graph
    Then the event video jumps to the time point user drags

  Scenario: User can jump to the time point by clicking backward -1
    When the user clicks backward -1 button
    Then the event video jumps backward 1 step

  Scenario: User can jump to the time point by clicking forward +1
    When the user clicks forward +1 button
    Then the event video jumps forward 1 step

  @LQ-12188
  Scenario: The FWD/LAT/TIME/GPS SPEED data displayed correctly while playing the event video
    When the user enters the event review page and event auto-plays
    Then the FWD/LAT/TIME/GPS SPEED data are displayed correctly when event video auto-plays

  Scenario: The FWD/LAT/TIME/GPS SPEED data displayed correctly while clicking progress bar
    When the user enters the event review page and clicks progress bar
    Then the FWD/LAT/TIME/GPS SPEED data are displayed correctly when user clicking progress bar

  Scenario: The FWD/LAT/TIME/GPS SPEED data displayed correctly while dragging progress bar
    When the user enters the event review page and drags progress bar
    Then the FWD/LAT/TIME/GPS SPEED data are displayed correctly when user dragging progress bar
