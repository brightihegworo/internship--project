from selenium.webdriver.common.by import By
from behave import given, when, then


#@when('Click the cart button')
#def click_cart(context):
   # context.driver.find_element(By.ID, 'nav-cart-count').click()


@then('Verify that the text {expected_result} is shown')
def verify_empty_cart_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//h2").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'