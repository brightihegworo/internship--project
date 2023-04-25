from pages.main_page import MainPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.product_detail_page = ProductDetailPage(self.driver)
        self.cart_page = CartPage(self.driver)