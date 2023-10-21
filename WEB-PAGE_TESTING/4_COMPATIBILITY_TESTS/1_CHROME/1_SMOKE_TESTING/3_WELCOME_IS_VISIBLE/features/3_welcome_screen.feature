Feature: Welcome screen

Scenario:  Welcome screen on browser
	Given  Open "https://qa-automation-practice.netlify.app/"
	When   Maximize window and "Welcome!" is on the first page
	Then   Close the browser