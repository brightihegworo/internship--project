from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    YOUR_CART = (By.CSS_SELECTOR, "h1.title")
    def verify_cart_page(self):
        expected_text = 'Your cart'
        actual_text = self.driver.find_element(*self.YOUR_CART).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

