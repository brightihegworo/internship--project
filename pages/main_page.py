from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    CLOSE_POPUP = (By.CSS_SELECTOR, "button.popup-close")
    PRODUCT = (By.XPATH, "//a[contains(text(), 'Under Eye Gel')]")

    def open_main_url(self):
        self.open_url('https://shop.cureskin.com/')

    def close_popup(self):
        self.wait_for_element_click(*self.CLOSE_POPUP)

    def click_on_product(self):
        self.wait_for_element_click(*self.PRODUCT)