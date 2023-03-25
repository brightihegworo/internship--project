from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page



class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart-count')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href='/New-Arrivals/b/?_encoding=UTF8&node=17020138011&ref_=sv_sl_6']")
    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS)

    def click_cart(self):
        self.click(*self.CART_ICON)

    def hover_lang_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        action = ActionChains(self.driver)
        action.move_to_element(lang_options)
        action.perform()
    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, alias):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')

    def hover_new_arrivals_options(self):
        new_arrivals_option = self.find_element(*self.NEW_ARRIVALS)
        action = ActionChains(self.driver)
        action.move_to_element(new_arrivals_option)
        action.perform()

    def verify_new_arrivals_options(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS)