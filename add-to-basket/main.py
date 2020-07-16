from selenium import webdriver
from pages.product import ProductPage


PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the" \
           "-shellcoders-handbook_209/?promo=newYear "

driver = webdriver.Firefox()
product_page = ProductPage(driver, PAGE_URL)
product_page.btn_add_to_basket.click()
product_page.solve_quiz_and_get_code()
