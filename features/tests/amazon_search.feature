
Feature: Test scenarios of search functionality using dropdown


  Scenario Outline: user can search an item by selecting a department from the dropdown
    Given Open amazon main page
    When select department by alias <department>
    And Input <item> into amazon search field
    And Click on main search icon
    Then verify <department_cat> department is selected
    Examples:
    | item   | department   | department_cat|
    | Toys   | baby-products| baby-products |
    | washer | appliances   | appliances    |