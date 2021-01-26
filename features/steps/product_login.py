from selenium.webdriver.common.by import By
from behave import given, when, then

# ORDER_BTN = By.XPATH, "//a[@id='nav-orders']"


@given('Open amazon page')
def amazon_page_open(context):
    context.driver.get("https://www.amazon.com/")


@when('user clicks orders')
def order_click(context):
    # context.driver.find_element(*ORDER_BTN).click()
    context.driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()


@then('SignIn page is opened')
def sign_in_page(context):
    page_title = context.driver.title
    print(page_title)
    assert page_title == "Amazon Sign-In"




