from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class CartPage(Page):
    YOUR_CART = (By.CSS_SELECTOR, "h1.title")
    MINUS_BUTTON = (By.CSS_SELECTOR, "button.quantity__button.no-js-hidden[name='minus']")
    EMPTY_CART = (By.CSS_SELECTOR, "h2.cart__empty-text")
    def verify_cart_page(self):
        expected_text = 'Your cart'
        actual_text = self.driver.find_element(*self.YOUR_CART).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

    def click_minus_button(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.MINUS_BUTTON)).click()

    def verify_cart_is_empty(self):

        assert self.driver.find_element(*self.EMPTY_CART).is_displayed()

