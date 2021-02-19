from selenium.webdriver.common.by import By
from behave import given, when, then


COLORS = (By.CSS_SELECTOR, "#variation_color_name li")
COLORS_TEXT = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('open the product page')
def open_product(context):
    context.driver.get("https://www.amazon.com/gp/product/B07BJKRR25/")


@then('verify that user can click through the colors')
def verify_colors(context):
    colors = context.driver.find_elements(*COLORS)

    colors_actual = []
    colors_expected = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage', 'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage', 'Vintage Light Wash', 'Washed Black']

    for i in range(len(colors)):
        colors[i].click()
        colors_text = context.driver.find_element(*COLORS_TEXT).text
        colors_actual.append(colors_text)
    assert colors_expected == colors_actual, f'expected {colors_expected} but got {colors_actual}'
