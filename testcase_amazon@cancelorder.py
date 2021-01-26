from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

# initialize driver
driver = webdriver.Chrome(executable_path="\\Users\\lngsvakti\\Desktop\\MyDocuments\\chromedriver.exe")
driver.delete_all_cookies()
driver.maximize_window()
driver.implicitly_wait(2)
# actions
driver.get("https://www.amazon.com/gp/help/customer/display.html")
search = driver.find_element(By.ID, "helpsearch")
search.send_keys("Cancel Order")
search.submit()
# verification
text_1 = driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text
print(text_1)
assert "Cancel Items or Orders" in text_1
text_2 = \
driver.find_element(By.XPATH, "//div[@class='cs-help-search-result-row']//a[contains(text(),'Cancel Items or Orders')]").text
print(text_2)
assert 'Cancel Items or Orders' in text_2

driver.quit()




