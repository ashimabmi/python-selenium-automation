from pages.base_page import Page
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage
from selenium.webdriver.common.by import By


class MainPage(Page):
    ORDER_BTN = (By.XPATH, "//a[@id='nav-orders']")
    CART_CLICK = (By.ID, 'nav-cart-text-container')
    INPUT_ITEM = (By.ID, 'twotabsearchtextbox')
    MAIN_SEARCH_ICON = (By.ID, 'nav-search-submit-button')

    def main_open_page(self):
        self.driver.get("https://www.amazon.com/")

    def order_click(self):
        self.click(*self.ORDER_BTN)
        return SignInPage

    def cart_click(self):
        self.click(*self.CART_CLICK)
        return CartPage

    def input_item(self, item):
        self.input_text(item, *self.INPUT_ITEM)

    def main_search_icon_click(self):
        self.click(*self.MAIN_SEARCH_ICON)







