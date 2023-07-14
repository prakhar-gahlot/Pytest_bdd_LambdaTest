Feature: Login

@LQ-9709
  Scenario: Reviewer lands on review page after clicking the Select button
	Given the user is in the Login page of New ARC and a user has Reviewer role in some companies
	When the user inputs valid username and password and the user clicks the Sign in button
	And the user select Reviewer role in the Role dropdown list and the user select one company in the company dropdown list and the user clicks the Select button
	Then the Review page is opened
