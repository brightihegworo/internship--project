# Created by brightihegworo at 4/20/23
Feature: Add to cart tests

#  Scenario: User can add and view product to the cart
#    Given Open Cureskin
#    When Close popup
#    When  Open Product Details page
#    When Click to add product to cart
#    Then Verify that the Subtotal is shown for confirmation
#    When Click View my cart
#    Then Verify user is taken to the cart page (Your Shopping Cart)


  Scenario: User can reduce the quantity of the product to 0
    Given Open Cureskin
    When Close popup
    When Click Search icon
    When Input Hydration Gel in the search bar
    When Click on the search product
    When Click to add product to cart
    When Click View my cart
    When Click minus button
    Then Verify the product is removed from cart


