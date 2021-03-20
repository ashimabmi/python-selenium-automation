from behave import given, when, then


@given('open amazon product page')
def open_product(context):
    context.driver.get('https://www.amazon.com/gp/product/B074TBCSC8')


@when('hovers over New Arrivals')
def hover_new_arrival(context):
    context.app.product_page.hover_new_arrival()


@then('verify deals is shown')
def verify_deals(context):
    context.app.product_page.verify_deals()

