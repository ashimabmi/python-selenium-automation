from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_PAGE = (By.XPATH, "//div[@class ='a-row sc-your-amazon-cart-is-empty']//h2")

    def verify_cart_page(self, message):
        self.verify_text(message, *self.CART_PAGE)


