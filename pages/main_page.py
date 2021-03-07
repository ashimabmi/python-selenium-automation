from pages.base_page import Page
from pages.sign_in_page import SignInPage
from selenium.webdriver.common.by import By


class MainPage(Page):
    ORDER_BTN = (By.XPATH, "//a[@id='nav-orders']")
    CART_CLICK = (By.ID, 'nav-cart-text-container')

    def main_open_page(self):
        self.driver.get("https://www.amazon.com/")

    def order_click(self):
        self.click(*self.ORDER_BTN)
        return SignInPage

    def cart_click(self):
        self.click(*self.CART_CLICK)


