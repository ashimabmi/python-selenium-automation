Feature: Test scenarios for amazon BestSeller page


  Scenario: user can open amazon BestSeller page
    Given Open amazon main page
    When user clicks on BestSellers
    Then 5 links are shown with their names
