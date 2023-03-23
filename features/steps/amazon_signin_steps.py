from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

#@given('Open Amazon page')
#def open_amazon(context):
   # context.driver.get('https://www.amazon.com/')


#@when('Click on Returns & Orders button')
#def click_returns_and_orders(context):
    #context.driver.find_element(By.ID, 'nav-orders').click()


#@then('Verify that the text {expected_result} is shown')
#def verify_signin_result(context, expected_result):
    #actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    #assert expected_result == actual_result


@then('Verify Sign In page opens')
def verify_signin_opened(context):
    context.app.signin_page.verify_signin_opened
    #context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))




