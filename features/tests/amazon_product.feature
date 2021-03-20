
Feature: Test scenarios for product


  Scenario: User can see the deals by hovering over New Arrivals
    Given open amazon product page
    When hovers over New Arrivals
    Then verify deals is shown

