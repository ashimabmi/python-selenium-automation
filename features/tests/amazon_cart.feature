
Feature: Test scenarios for cart functionality on amazon page


  Scenario: user sees an empty cart when clicks on cart icon of amazon page
    Given Open amazon main page
    When User clicks on cart icon
    Then result shows Your Amazon Cart is empty

