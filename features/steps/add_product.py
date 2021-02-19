from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_CLICK = (By.XPATH, "//span[@data-component-type='s-product-image']//a")
ADD_CART_CLICK = (By.ID, 'add-to-cart-button')
ADD_CART = (By.XPATH, "//div[@id='huc-v2-order-row-confirm-text']//h1")
INPUT_ITEM = (By.ID, 'twotabsearchtextbox')
MAIN_SEARCH_ICON = (By.ID, 'nav-search-submit-button')
CART_COUNT = (By.XPATH, "//span[@id='nav-cart-count']")
PRODUCT_QTY = (By.XPATH, "//select[@id='quantity']//option")


@when('Input {item} into amazon search field')
def input_item(context, item):
    search = context.driver.find_element(*INPUT_ITEM)
    search.send_keys(item)


@when('Click on main search icon')
def main_search_icon(context):
    context.driver.find_element(*MAIN_SEARCH_ICON).click()


@when('Click on the product')
def product_click(context):
    product = context.driver.find_elements(*PRODUCT_CLICK)
    product[0].click()


@when('select the product quantity {number}')
def product_qty(context, number):

    selector = context.driver.find_elements(*PRODUCT_QTY)
    selector[int(number)-1].click()


@when('Click on add to cart')
def add_cart_click(context):
    click_cart = context.driver.find_element(*ADD_CART_CLICK)
    click_cart.click()


@then('Product is {expected_text} message is shown')
def add_cart(context, expected_text):
    message1 = context.driver.find_element(*ADD_CART).text
    print(message1)
    assert expected_text in message1


@then('cart count is shown as {item_count}')
def cart_count(context, item_count):
    message2 = context.driver.find_element(*CART_COUNT).text
    print(message2)
    assert item_count in message2



