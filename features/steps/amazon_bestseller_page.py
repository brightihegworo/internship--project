from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

LINKS = (By.XPATH, "//div[contains(@class, '_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq')]/ul/li/div/a")



@then('Verify page has {expected_count} links')
def verify_cart_count(context, expected_count):
    all_links = context.driver.find_elements(*LINKS)
    actual_count = len(all_links)
    assert expected_count == str(actual_count), f'Expected {expected_count} but got actual {actual_count}'