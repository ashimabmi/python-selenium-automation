from selenium.webdriver.common.by import By
from behave import given, when, then

CART_CLICK = (By.ID, 'nav-cart-text-container')
CART_PAGE = (By.XPATH, "//div[@class ='a-row sc-your-amazon-cart-is-empty']//h2")


@given('Open amazon main page')
def amazon_page_open(context):
    context.driver.get("https://www.amazon.com/")


@when('User clicks on cart icon')
def cart_click(context):
    context.driver.find_element(*CART_CLICK).click()


@then('result shows {message}')
def cart_page(context, message):
    cart_text = context.driver.find_element(*CART_PAGE).text
    print(cart_text)
    assert message in cart_text, "expected message is '{}' but got actual message '{}'".format(message, cart_text)





