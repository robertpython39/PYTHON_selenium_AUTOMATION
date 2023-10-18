Feature: Web automation with Selenium

Scenario: Open a specific webpage and maximize the window
    Given Open web browser "https://qa-automation-practice.netlify.app/"
    When  Maximize the web browser window
    Then  Welcome screen should be "Welcome"
