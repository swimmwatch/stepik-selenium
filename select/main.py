from selenium import webdriver
from selenium.webdriver.support.ui import Select

PAGE_URL = "http://suninjuly.github.io/selects1.html"

driver = webdriver.Firefox()
driver.get(PAGE_URL)

# get elements
dropdown_input = driver.find_element_by_id("dropdown")
dropdown = Select(dropdown_input)
submit_btn = driver.find_element_by_css_selector("[type=\"submit\"]")

num1 = driver.find_element_by_id("num1").text
num2 = driver.find_element_by_id("num2").text
res = int(num1) + int(num2)

# type answer
dropdown.select_by_value(str(res))
submit_btn.click()

# driver.close()
