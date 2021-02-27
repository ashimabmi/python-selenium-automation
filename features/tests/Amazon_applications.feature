
Feature: Test scenarios for amazon application page


  Scenario: User can open and close Amazon Applications
    Given Open Amazon T&C page
    When store original windows
    And click on Amazon applications link
    And switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original