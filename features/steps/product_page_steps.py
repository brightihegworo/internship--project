from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.a-price.priceToPay span.a-offscreen')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/EDSTAR-Batwing-Sleeves-Sweaters-Pullovers/dp/{product_id}/')
@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(4)


@when('Store product name and price')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')
    context.product_price = context.driver.find_element(*PRODUCT_PRICE)
    print(f'Current product price: {context.product_price}')


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    all_colors_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_colors_options)
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy']

    actual_colors = []
    for color in all_colors_options[:5]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'


