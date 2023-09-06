Feature: Video Player

  @LQ-11160
  Scenario: P1_Video Player Tests
  	#Scenario: User see event details after clicking one event review ID
    Given "Reviewer" logs in ARC
    When "Reviewer" filtered out some events in new ARC and the user clicks one event review ID and the user checks the event details above event video
    Then Review ID is displayed correctly and Trigger is displayed correctly and Record Date is displayed based on local time zone and format is YYYY-MM-DD hh:mm AM/PM
    And Vehicle ID is displayed as vehicle name and Vehicle type is displayed correctly and Seatbelt is displayed correctly and Audio is displayed correctly and FPS is displayed correctly
