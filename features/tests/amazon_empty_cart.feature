# Created by brightihegworo at 2/21/23
Feature: Empty cart feature


  Scenario: User can see empty cart message
    Given Open Amazon Page
    When Click the cart button
    Then Verify 'Your Amazon Cart is empty.' text present
