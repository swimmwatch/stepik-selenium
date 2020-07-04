from selenium import webdriver
import time

browser = webdriver.Firefox()
try:
    link = "https://suninjuly.github.io/registration2.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_field = browser.find_element_by_css_selector('.form-control.first[required=""]')
    last_name_field = browser.find_element_by_css_selector('.form-control.second[required=""]')
    email_field = browser.find_element_by_css_selector('.form-control.third[required=""]')
    first_name_field.send_keys('Name')
    last_name_field.send_keys('LastName')
    email_field.send_keys('mai@mai.ru')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на
    # странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
