from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_PAGE = (By.XPATH, "//div[@class ='a-row sc-your-amazon-cart-is-empty']//h2")
    ADD_CART = (By.XPATH, "//div[@id='huc-v2-order-row-confirm-text']//h1")
    CART_COUNT = (By.XPATH, "//span[@id='nav-cart-count']")

    def verify_cart_page(self, message):
        self.verify_text(message, *self.CART_PAGE)

    def verify_add_cart(self, expected_text):
        self.verify_text(expected_text, *self.ADD_CART)

    def verify_cart_count(self, item_count):
        self.verify_text(item_count, *self.CART_COUNT)


