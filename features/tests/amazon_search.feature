# Created by brightihegworo at 2/16/23
#Feature: Amazon search tests


  Scenario: User can search for coffee on Amazon
    Given Open Amazon page
    When Input text coffee
    When Click on search button
    Then Verify that the text "coffee" is shown


  Scenario: User can search for table on Amazon
    Given Open Amazon page
    When Input text table
    When Click on search button
    Then Verify that the text "table" is shown