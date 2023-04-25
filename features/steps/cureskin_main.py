from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


CLOSE_POPUP = (By.CSS_SELECTOR, "button.popup-close")
PRODUCT = (By.XPATH, "//a[contains(text(), 'Under Eye Gel')]")

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



