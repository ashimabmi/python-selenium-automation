
from behave import given, when, then


@when('Input {item} into amazon search field')
def input_item(context, item):
    context.app.main_page.input_item(item)


@when('Click on main search icon')
def main_search_icon(context):
    context.app.main_page.main_search_icon_click()


@when('Click on the product')
def product_click(context):
    context.app.product_page.product_click()


@when('select the product quantity {number}')
def product_qty(context, number):
    context.app.product_page.product_qty_click(number)


@when('Click on add to cart')
def add_cart_click(context):
    context.app.product_page.add_cart_click()


@then('Product is {expected_text} message is shown')
def add_cart(context, expected_text):
    context.app.cart_page.verify_add_cart(expected_text)


@then('cart count is shown as {item_count}')
def cart_count(context, item_count):
    context.app.cart_page.verify_cart_count(item_count)



