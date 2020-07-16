from .base import BasePage


class ProductPage(BasePage):

    def __init__(self, browser, link):
        super(ProductPage, self).__init__(browser, link)

        self.btn_add_to_basket = self.browser.find_element_by_class_name("btn-add-to-basket")