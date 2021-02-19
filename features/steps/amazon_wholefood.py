from selenium.webdriver.common.by import By
from behave import given, when, then


PRODUCT_DETAILS = (By.XPATH, "//ul[@class='s-result-list s-col-3 wfm-desktop-list-font-unset s-height-equalized']//li//div[@class='a-row']//span")


@given('open amazon wholefoods page')
def open_wholefood_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('verify the text with product name')
def verify_product(context):
    product_details = context.driver.find_elements(*PRODUCT_DETAILS)
    for i in range(len(product_details)):
        name = product_details[i].text
        print(name)

        if i % 5 == 0 or i == 0:
            assert product_details[i].text != "", f'expected some product name but got {product_details[i].text}'
            if i != 0:
                assert 'Regular' in product_details[i-1].text, f'expected {"Regular"} but got {product_details[i-1].text}'













