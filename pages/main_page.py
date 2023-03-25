from pages.base_page import Page


class MainPage(Page):

    def open_main_url(self):
        self.open_url('https://www.amazon.com/')

    def open_amazon_product(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')