from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ADD_TO_CART = (By.CSS_SELECTOR, "button[type='submit'].product-form__submit.button.button--secondary")
ADD_TO_CART_CONFIRM = (By.CSS_SELECTOR, "h3.label")
VIEW_CART = (By.CSS_SELECTOR, "div.button-container a[href='/cart']")


@when('Click to add product to cart')
def add_to_cart(context):
    context.app.product_detail_page.add_to_cart()
    sleep(5)

    #context.driver.find_element(*ADD_TO_CART).click()


@when("Click View my cart")
def click_view_cart(context):
    context.app.product_detail_page.click_view_cart()
    # context.driver.wait.until(EC.element_to_be_clickable(VIEW_CART)).click()
    # sleep(3)


@then('Verify that the Subtotal is shown for confirmation')
def verify_add_to_cart_confirm(context):
    context.app.product_detail_page.verify_add_to_cart_confirm()
    # expected_text = 'Subtotal'
    # actual_text = context.driver.find_element(*ADD_TO_CART_CONFIRM).text
    # assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


