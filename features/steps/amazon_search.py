from behave import given, when, then


@when('select department by alias {alias}')
def select_department(context, alias):
    context.app.main_page.select_department(alias)


@then('verify {department} department is selected')
def verify_department(context, department):
    context.app.product_page.verify_department(department)
