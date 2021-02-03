from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.ID, 'helpsearch')
SEARCH_RESULT = (By.XPATH, "//div[@class='help-content']//h1")


@given('Open amazon search help page')
def amazon_help_search_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@when('input {search} into search help field and enter')
def search_input(context, search):
    element = context.driver.find_element(*SEARCH_INPUT)
    element.send_keys(search, Keys.ENTER)


@then('search result contains {results} text')
def search_result(context, results):
    text_1 = context.driver.find_element(*SEARCH_RESULT).text
    print(text_1)
    assert results in text_1, "expected word '{}' in message but got actual word '{}'".format(results, text_1)






