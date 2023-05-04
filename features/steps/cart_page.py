from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

YOUR_CART = (By.CSS_SELECTOR, "h1.title")
MINUS_BUTTON = (By.CSS_SELECTOR, "button.quantity__button.no-js-hidden[name='minus']")
EMPTY_CART = (By.CSS_SELECTOR, "h2.cart__empty-text")


@when("Click minus button")
def click_minus_button(context):
    context.app.cart_page.click_minus_button()
    #context.driver.wait.until(EC.element_to_be_clickable(MINUS_BUTTON)).click()


@then("Verify user is taken to the cart page (Your Shopping Cart)")
def verify_cart_page(context):
    context.app.cart_page.verify_cart_page()
    # expected_text = 'Your cart'
    # actual_text = context.driver.find_element(*YOUR_CART).text
    # assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


@then("Verify the product is removed from cart")
def verify_cart_is_empty(context):
    sleep(5)
    context.app.cart_page.verify_cart_is_empty()
    #assert context.driver.find_element(*EMPTY_CART).is_displayed()