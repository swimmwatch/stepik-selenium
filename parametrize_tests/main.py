import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CORRECT_STR = "Correct!"


@pytest.fixture(scope="function")
def browser():
    print("Start browser for test..")
    browser = webdriver.Firefox()
    browser.implicitly_wait(7)
    yield browser
    print("Quit browser..")
    browser.quit()


@pytest.mark.parametrize("link", [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_collect_msg(browser, link):
    browser.get(link)

    textarea = browser.find_element_by_tag_name("textarea")
    submit_btn = browser.find_element_by_class_name("submit-submission")

    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))

    WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )

    submit_btn.click()

    result_msg = browser.find_element_by_class_name("smart-hints__hint")

    assert result_msg.text == CORRECT_STR
