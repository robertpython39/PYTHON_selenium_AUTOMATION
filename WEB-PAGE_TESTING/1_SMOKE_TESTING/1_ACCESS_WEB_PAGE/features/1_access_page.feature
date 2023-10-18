Feature: Smoke testing

Scenario: Open the webpage and access the link
    Given Open web browser "https://qa-automation-practice.netlify.app/"
    When  Maximize the web browser window

Scenario: Request is 200 for the website
	Given Make requeste to "https://qa-automation-practice.netlify.app/"
	When  Respone is 200
	Then  I close the browser window