from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CLOSE_POPUP = (By.CSS_SELECTOR, "button.popup-close")
PRODUCT = (By.XPATH, "//a[contains(text(), 'Under Eye Gel')]")
SEARCH_ICON = (By.CSS_SELECTOR, ".icon.icon-search.modal__toggle-open[role='presentation']")
SEARCH_BAR = (By.CSS_SELECTOR, "#Search-In-Modal.search__input.field__input[type='search'][placeholder='Search']")
SEARCH_PRODUCT = (By.CSS_SELECTOR, ".predictive-search__item-content")

@given('Open Cureskin')
def open_cureskin(context):
    context.app.main_page.open_main_url()
    # context.driver.get('https://shop.cureskin.com/')


@when('Close popup')
def close_popup(context):
    context.app.main_page.close_popup()
    # context.driver.wait.until(EC.element_to_be_clickable(CLOSE_POPUP)).click()
    # sleep(3)


@when('Open Product Details page')
def click_on_product(context):
    context.app.product_detail_page.open_product()
     # element = context.driver.find_element(*PRODUCT)
     # context.driver.execute_script("arguments[0].click();", element)


@when("Click Search icon")
def click_search_icon(context):
    context.app.main_page.click_search_icon()
     #context.driver.find_element(*SEARCH_ICON).click()


@when("Input {text} in the search bar")
def input_text_in_search_bar(context, text):
    context.app.main_page.input_text_in_search_bar(text)
    #context.driver.find_element(*SEARCH_BAR).send_keys(text)


@when("Click on the search product")
def click_on_search_product(context):
    context.app.main_page.click_on_search_product()
    #context.driver.wait.until(EC.element_to_be_clickable(SEARCH_PRODUCT)).click()








