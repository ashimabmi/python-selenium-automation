from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import Page
from pages.cart_page import CartPage


class ProductPage(Page):
    PRODUCT_CLICK = (By.XPATH, "//span[@data-component-type='s-product-image']//a")
    PRODUCT_QTY = (By.XPATH, "//select[@id='quantity']//option")
    ADD_CART_CLICK = (By.ID, 'add-to-cart-button')
    NEW_ARRIVAL_LI = (By.XPATH, "//div[@id='nav-subnav']//span[contains(text(),'New Arrivals')]")
    DEALS_POPUP = (By.ID, 'nav-flyout-aj:https://softlines-trova.s3-us-west-2.amazonaws.com/prod/US/mediaservice/megamenucreator_basic_en_US.json:subnav-sl-megamenu-8:0')
    SELECTED_DEPARTMENT_CAT = (By.CSS_SELECTOR, "#nav-subnav[data-category='{DEPT_SUBSTRING}']")

    def _get_locator_(self, department):
        return [self.SELECTED_DEPARTMENT_CAT[0], self.SELECTED_DEPARTMENT_CAT[1].replace('{DEPT_SUBSTRING}', department)]

    def product_click(self):
        self.click(*self.PRODUCT_CLICK)

    def product_qty_click(self, number):
        selector = self.driver.find_elements(*self.PRODUCT_QTY)
        selector[int(number)-1].click()

    def add_cart_click(self):
        self.click(*self.ADD_CART_CLICK)
        return CartPage

    def hover_new_arrival(self):
        new_arrival_li = self.find_element(*self.NEW_ARRIVAL_LI)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrival_li)
        actions.perform()

    def verify_deals(self):
        self.wait_for_element_appear(*self.DEALS_POPUP)

    def verify_department(self, department):
        locator = self._get_locator_(department)
        self.wait_for_element_appear(*locator)





