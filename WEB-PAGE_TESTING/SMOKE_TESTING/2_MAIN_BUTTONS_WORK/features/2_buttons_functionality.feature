Feature: Buttons Functionality

Scenario: Open browser and check buttons
	Given  Open the webpage "https://qa-automation-practice.netlify.app/"
	When   Maximize the window
	Then   Press "Contact" button
	Then   Press "Home" button
	Then   Minimize the webpage
