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

	@LQ-10595
	Scenario: Search new event by single Review ID
		When the user input a valid New event Review ID and the user clicks "Filter" button
		Then the related event is filtered out under the New tab and the event count of New tab is shown
		And the event list shows columns: "REVIEW ID","EVENT ID","CREATION DATE","VEHICLE NAME","ER SERIAL"

	Scenario: Search returned event by single Review ID
		When the user input returned event review ID in the filter under the Returned tab and the user clicks "Filter" button
		Then the related event is filtered under the Returned tab and the event count of returned tab is shown
		And the event list shows columns: "REVIEW ID","EVENT ID","CREATION DATE","VEHICLE NAME","ER SERIAL"

	@LQ-11162
	Scenario: System loads and automatically plays video clip of event upon the Reviewer landing on page
		When the user clicks one reviewID
		Then the event review page is opened and the both front and rear camera views are shown and the video automatically plays
