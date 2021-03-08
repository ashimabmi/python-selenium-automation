from selenium.webdriver.common.by import By

from pages.base_page import Page
from pages.cart_page import CartPage


class ProductPage(Page):
    PRODUCT_CLICK = (By.XPATH, "//span[@data-component-type='s-product-image']//a")
    PRODUCT_QTY = (By.XPATH, "//select[@id='quantity']//option")
    ADD_CART_CLICK = (By.ID, 'add-to-cart-button')

    def product_click(self):
        self.click(*self.PRODUCT_CLICK)

    def product_qty_click(self, number):
        selector = self.driver.find_elements(*self.PRODUCT_QTY)
        selector[int(number)-1].click()

    def add_cart_click(self):
        self.click(*self.ADD_CART_CLICK)
        return CartPage





