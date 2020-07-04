import os
from selenium import webdriver


PAGE_URL = "http://suninjuly.github.io/file_input.html"

driver = webdriver.Firefox()
driver.get(PAGE_URL)

# get elements
firstname_input = driver.find_element_by_css_selector("[name=firstname]")
lastname_input = driver.find_element_by_css_selector("[name=lastname]")
email_input = driver.find_element_by_css_selector("[name=email]")
file_upload_input = driver.find_element_by_id("file")
submit_btn = driver.find_element_by_css_selector("[type=\"submit\"]")

# type answer
firstname_input.send_keys("Dmitry")
lastname_input.send_keys("Vasiliev")
email_input.send_keys("vaas@gmail.com")

path = os.path.abspath("input.txt")
file_upload_input.send_keys(path)

submit_btn.click()

# driver.close()
