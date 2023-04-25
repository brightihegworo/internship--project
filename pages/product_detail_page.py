from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductDetailPage(Page):
    ADD_TO_CART = (By.CSS_SELECTOR, "button[type='submit'].product-form__submit.button.button--secondary")
    ADD_TO_CART_CONFIRM = (By.CSS_SELECTOR, "h3.label")
    VIEW_CART = (By.CSS_SELECTOR, "div.button-container a[href='/cart']")
    PRODUCT = (By.XPATH, "//a[contains(text(), 'Under Eye Gel')]")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)


    def click_view_cart(self):
        self.wait_for_element_click(*self.VIEW_CART)


    def verify_add_to_cart_confirm(self):
        expected_text = 'Subtotal'
        actual_text = self.driver.find_element(*self.ADD_TO_CART_CONFIRM).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'


    def open_product(self):
        element = self.driver.find_element(*self.PRODUCT)
        self.driver.execute_script("arguments[0].click();", element)




