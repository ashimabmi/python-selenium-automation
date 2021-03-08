
from behave import given, when, then


@given('Open amazon main page')
def amazon_page_open(context):
    context.app.main_page.main_open_page()


@when('User clicks on cart icon')
def cart_click(context):
    context.app.main_page.cart_click()


@then('result shows {message}')
def verify_cart_page(context, message):
    context.app.cart_page.verify_cart_page(message)







