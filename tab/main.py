import math
from selenium import webdriver
from time import sleep


def calc(x: str):
    return str(math.log(abs(12*math.sin(int(x)))))


PAGE_URL = "http://suninjuly.github.io/redirect_accept.html"

driver = webdriver.Firefox()
driver.get(PAGE_URL)

# call alert box
submit_btn = driver.find_element_by_css_selector("[type=\"submit\"]")
submit_btn.click()

another_tabname = driver.window_handles[1]
driver.switch_to.window(another_tabname)

sleep(1)

# get elements
answer_input = driver.find_element_by_id("answer")
submit_btn = driver.find_element_by_css_selector("[type=\"submit\"]")

value = driver.find_element_by_id("input_value").text
answer = calc(value)

# type answer
answer_input.send_keys(answer)
submit_btn.click()

# driver.close()
