Feature: Amazon signin test


  #Scenario: User can reach the signup page
    #Given Open Amazon page
   # When Click on Returns & Orders button
    #Then Verify that the text Sign in is shown

Scenario: Sign in page can be opened from Sign In popup
  Given Open Amazon page
  When Click Sign In from popup
  Then Verify Sign In page opens


Scenario: Sign in popup is visible for a few seconds
  Given Open Amazon page
  Then Verify Sign In popup shown
  When Wait for 8 sec
  Then Verify Sign in popup disappears