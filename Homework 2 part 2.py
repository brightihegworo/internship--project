from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/brightihegworo/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

print(actual_result)

assert expected_result == actual_result

print('Passed')