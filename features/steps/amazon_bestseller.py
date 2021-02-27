from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BESTSELLERS = (By.CSS_SELECTOR, "#nav-xshop a")
LINKS = (By.XPATH, "//div[@id='zg_tabs']//ul//li")
LINKS_CLICK = (By.CSS_SELECTOR, "div[id='zg_tabs'] a:nth-child(1)")
HEADER_TXT = (By.ID, 'zg_banner_text_wrapper')


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


@then('clicks on each top link and new page opens')
def click_link_new_page(context):
    links_click = context.driver.find_elements(*LINKS_CLICK)
    for i in range(len(links_click)):

        if links_click[i].text in ['Best Sellers', 'New Releases', 'Movers & Shakers', 'Most Wished For', 'Gift Ideas']:
            links_click[i].click()
            txt = context.driver.find_element(*HEADER_TXT).text
            links_click = context.driver.find_elements(*LINKS_CLICK)
            assert txt.find(links_click[i].text) != -1, 'expected text is not in actual text'
































