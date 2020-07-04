import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class SignUpForm(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)

    def test_success_sign_up(self):
        link = "https://suninjuly.github.io/registration1.html"
        self.driver.get(link)

        first_name_field = self.driver.find_element_by_css_selector(
            '.form-control.first[required=""]')
        last_name_field = self.driver.find_element_by_css_selector(
            '.form-control.second[required=""]')
        email_field = self.driver.find_element_by_css_selector(
            '.form-control.third[required=""]')
        first_name_field.send_keys('Name')
        last_name_field.send_keys('LastName')
        email_field.send_keys('mai@mai.ru')

        button = self.driver.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = self.driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!",
                         welcome_text)

    def test_failed_sign_up(self):
        def test():
            link = "https://suninjuly.github.io/registration2.html"
            self.driver.get(link)

            first_name_field = self.driver.find_element_by_css_selector(
                '.form-control.first[required=""]')
            last_name_field = self.driver.find_element_by_css_selector(
                '.form-control.second[required=""]')
            email_field = self.driver.find_element_by_css_selector(
                '.form-control.third[required=""]')
            first_name_field.send_keys('Name')
            last_name_field.send_keys('LastName')
            email_field.send_keys('mai@mai.ru')

            button = self.driver.find_element_by_css_selector("button.btn")
            button.click()

            welcome_text_elt = self.driver.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully "
                             "registered!",
                             welcome_text)

        self.assertRaises(NoSuchElementException, test)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
