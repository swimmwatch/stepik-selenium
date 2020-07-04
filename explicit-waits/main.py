import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x: str):
    return str(math.log(abs(12*math.sin(int(x)))))


PAGE_URL = "http://suninjuly.github.io/explicit_wait2.html"

driver = webdriver.Firefox()
driver.get(PAGE_URL)

text = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

book_btn = driver.find_element_by_id("book")
book_btn.click()

# get elements
answer_input = driver.find_element_by_id("answer")
submit_btn = driver.find_element_by_css_selector("[type=\"submit\"]")

value = driver.find_element_by_id("input_value").text
answer = calc(value)

# type answer
answer_input.send_keys(answer)
submit_btn.click()

# driver.close()
