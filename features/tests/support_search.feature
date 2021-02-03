
Feature: Test scenarios for support search functionality


  Scenario: User can search for Cancelling an order on Amazon
    Given Open amazon search help page
    When input cancel order into search help field and enter
    Then search result contains Cancel Items or Orders text