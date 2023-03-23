from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    EMPTY_CART = (By.XPATH, "//h2").text

    def verify_empty_cart(self):
        self.verify_empty_cart()