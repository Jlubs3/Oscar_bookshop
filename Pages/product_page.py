# pages/product_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

    def add_to_basket(self):
        add_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_see_success_message(self):
        product_name = self.browser.find_element(*self.PRODUCT_NAME).text
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert product_name == success_message, \
            f"Expected product name '{product_name}' in the success message, but got '{success_message}'"

    def should_see_correct_basket_total(self):
        product_price = self.browser.find_element(*self.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert product_price == basket_total, \
            f"Expected basket total '{product_price}', but got '{basket_total}'"
