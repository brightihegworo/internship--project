from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
# Create Account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# Your Name
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
# Email
driver.find_element(By.CSS_SELECTOR, '#ap_email')
# Password
driver.find_element(By.CSS_SELECTOR, '#ap_password')
# Passwords must be at least 6 characters.
driver.find_element(By.CSS_SELECTOR, 'div.a-alert-content')
# Re-enter Password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# Continue
driver.find_element(By.CSS_SELECTOR, '#continue')
# Condition of Use
driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088"]')
# Privacy Notice
driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496"]')
#Sign in
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')

