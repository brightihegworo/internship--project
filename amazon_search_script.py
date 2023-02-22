from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/brightihegworo/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/')


driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')

driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"table"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(actual_result)

assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print('Test case passed')

driver.quit()