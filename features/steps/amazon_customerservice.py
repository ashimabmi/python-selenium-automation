from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#CUSTOMER_SERVICE = (By.CSS_SELECTOR, "#nav-xshop a:nth-child(3)")
HEAD_TEXT = (By.CSS_SELECTOR, "div.a-section.ss-landing-container h1")
expected_text1 = "Hello. What can we help you with?"
SUB_TEXT = (By.CSS_SELECTOR, "div.a-section.ss-landing-container-wide h2")
expected_text2 = "Some things you can do here"
SEARCH = (By.CSS_SELECTOR, "div.a-spacing-top-extra-large.ss-landing-container-wide")
expected_text3 = 'Search the help library   Type something like, "question about a charge"'
HELP_TOPICS = (By.XPATH, "//div[@class='a-span12 a-column a-spacing-top-small']//h1")
expected_text4 = "Browse Help Topics"
IMAGE = (By.CSS_SELECTOR, "img.csg-hb-promo")
expected_size1 = 8
expected_size2 = 12


@given('Open amazon Customer Service page')
def customer_service(context):
    #context.driver.find_element(*CUSTOMER_SERVICE).click()
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('UI elements are present of the page')
def ui_elements(context):
    text1 = context.driver.find_element(*HEAD_TEXT).text
    print(text1)
    assert expected_text1 == text1, f'expected text is {expected_text1} but got {text1}'

    text2 = context.driver.find_element(*SUB_TEXT).text
    print(text2)
    assert expected_text2 == text2, f'expected text is {expected_text2} but got {text2}'

    elements = context.driver.find_elements(By.XPATH, "//div[@class='a-column a-span9 a-span-last']")
    actual = len(elements)
    for item in elements:
        print(item.text)
    assert expected_size1 == actual

    search_option = context.driver.find_element(*SEARCH)
    text3 = search_option.text
    print(text3)
    assert expected_text3 == text3

    text4 = context.driver.find_element(*HELP_TOPICS).text
    assert expected_text4 == text4

    elements2 = context.driver.find_elements(By.XPATH, "//ul[@id='category-section']//li")
    actual_size = len(elements2)
    for option in elements2:
        print(option.text)
    assert expected_size2 == actual_size

    image = context.driver.find_element(*IMAGE)
    print(image.get_attribute("src"))
    if image.get_attribute("src") != 0:
        print("True")
        assert True















