
from behave import given, when, then


@given('Open amazon page')
def amazon_page_open(context):
    context.app.main_page.main_open_page()


@when('user clicks orders')
def order_click(context):
    context.app.main_page.order_click()


@then('SignIn page is opened')
def sign_in_page(context):
    context.app.sign_in_page.sign_in_page_title('Amazon Sign-In')



