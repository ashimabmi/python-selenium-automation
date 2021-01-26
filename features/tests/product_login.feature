# Created by lngsvakti at 1/25/2021
Feature:test scenarios for login functionality


  Scenario:Logged out user sees Sign in page when clicking Orders
    Given Open amazon page
    When user clicks orders
    Then SignIn page is opened

