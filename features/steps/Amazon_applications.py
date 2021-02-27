from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

LINK = (By.XPATH, "//a[@href='https://www.amazon.com/gp/feature.html?docId=1000625601']")


@given('Open Amazon T&C page')
def open_amazon_terms_conditions_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('click on Amazon applications link')
def click_amazon_applications(context):
    context.driver.find_element(*LINK).click()


@when('switch to the newly opened window')
def new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(context.new_window)


@then('Amazon app page is opened')
def verify_amazon_app_page(context):
    assert context.driver.title == "Amazon Mobile Shopping Apps"


@then('User can close new window and switch back to original')
def verify_close_new_window_switch_original(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)




