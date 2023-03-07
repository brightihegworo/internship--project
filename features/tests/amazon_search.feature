# Created by brightihegworo at 2/16/23
Feature: Amazon search tests


  #Scenario: User can search for coffee on Amazon
    #Given Open Amazon page
    #When Input text coffee
    #When Click on search button
    #Then Verify that the text "coffee" is shown


  #Scenario: User can search for table on Amazon
    #Given Open Amazon page
    #When Input text table
    #When Click on search button
    #Then Verify that the text "table" is shown

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Tritan Farm to table Pitcher
    When Click on search button
    And Click on the first product
    And Store product name and price
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product and price


  #Scenario: User can open amazon BestSellers page
   # Given Open Amazon page
    #When Click on All button
    #When Click on Bestseller
    #Then Verify page has 5 links

