# Created by brightihegworo at 4/20/23
Feature: Add to cart tests

  Scenario: User can add and view product to the cart
    Given Open Cureskin
    When Close popup
    When  Open Product Details page
    When Click to add product to cart
    Then Verify that the Subtotal is shown for confirmation
    When Click View my cart
    Then Verify user is taken to the cart page (Your Shopping Cart)