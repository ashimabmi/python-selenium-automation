from selenium.webdriver.common.by import By
from behave import given, when, then

BESTSELLERS = (By.CSS_SELECTOR, "#nav-xshop a")
LINKS = (By.XPATH, "//div[@id='zg_tabs']//ul//li")


@when('user clicks on BestSellers')
def click_bestseller(context):
    context.driver.find_element(*BESTSELLERS).click()


@then('{num} links are shown with their names')
def verify_links(context, num):
    best_li = context.driver.find_elements(*LINKS)
    actual_num = len(best_li)
    assert int(num) == actual_num
    item_li = []
    for item in best_li:
        item_text = item.text
        print(item_text)
        item_li.append(item_text)
    print(item_li)
    expected_li = ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']
    assert expected_li == item_li
