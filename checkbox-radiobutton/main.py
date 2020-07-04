import math
from selenium import webdriver


def calc(x: str):
    return str(math.log(abs(12*math.sin(int(x)))))


PAGE_URL = "http://suninjuly.github.io/math.html"

driver = webdriver.Firefox()
driver.get(PAGE_URL)



driver.close()
