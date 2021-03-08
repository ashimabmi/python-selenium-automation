
Feature: Test scenarios for add product functionality


  Scenario Outline: user can search and add a product into the cart
    Given Open amazon main page
    When Input <item> into amazon search field
    And Click on main search icon
    And Click on the product
    And select the product quantity <number>
    And Click on add to cart
    Then Product is Added to Cart message is shown
    Then cart count is shown as <item_count>
    Examples:
    | item      |number|item_count|
    | baby Toys | 3    | 3        |
    | craft     | 2    | 2        |
