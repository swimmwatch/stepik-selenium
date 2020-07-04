import math
from selenium import webdriver


def calc(x: str):
    return str(math.log(abs(12*math.sin(int(x)))))


PAGE_URL = "http://SunInJuly.github.io/execute_script.html"

driver = webdriver.Firefox()
driver.get(PAGE_URL)

# get elements
answer_input = driver.find_element_by_id("answer")
robot_checkbox = driver.find_element_by_id("robotCheckbox")
robot_radiobtn = driver.find_element_by_id("robotsRule")
submit_btn = driver.find_element_by_css_selector("[type=\"submit\"]")

value = driver.find_element_by_id("input_value").text
answer = calc(value)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# type answer
answer_input.send_keys(answer)
robot_checkbox.click()
robot_radiobtn.click()
submit_btn.click()

# driver.close()
