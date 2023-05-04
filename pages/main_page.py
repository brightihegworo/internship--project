from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

class MainPage(Page):
    CLOSE_POPUP = (By.CSS_SELECTOR, "button.popup-close")
    PRODUCT = (By.XPATH, "//a[contains(text(), 'Under Eye Gel')]")
    SEARCH_ICON = (By.CSS_SELECTOR, ".icon.icon-search.modal__toggle-open[role='presentation']")
    SEARCH_BAR = (By.CSS_SELECTOR, "#Search-In-Modal.search__input.field__input[type='search'][placeholder='Search']")
    SEARCH_PRODUCT = (By.CSS_SELECTOR, ".predictive-search__item-content")

    def open_main_url(self):
        self.open_url('https://shop.cureskin.com/')

    def close_popup(self):
        self.wait_for_element_click(*self.CLOSE_POPUP)

    def click_on_product(self):
        self.wait_for_element_click(*self.PRODUCT)

    def click_search_icon(self):
        self.driver.find_element(*self.SEARCH_ICON).click()

    def input_text_in_search_bar(self, text):
        self.driver.find_element(*self.SEARCH_BAR).send_keys(text)

    def click_on_search_product(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.SEARCH_PRODUCT)).click()