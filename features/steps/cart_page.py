from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


YOUR_CART = (By.CSS_SELECTOR, "h1.title")


@then("Verify user is taken to the cart page (Your Shopping Cart)")
def verify_cart_page(context):
    context.app.cart_page.verify_cart_page()
    # expected_text = 'Your cart'
    # actual_text = context.driver.find_element(*YOUR_CART).text
    # assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'