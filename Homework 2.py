from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')

#Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email Field
driver.find_element(By.ID, "ap_email")

#Continue button
driver.find_element(By.ID, "continue")

#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

#Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

#Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

#Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use?')]")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice?')]")



