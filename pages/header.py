from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_BTN = (By.XPATH, "//a[@data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.XPATH, "//a[@data-test='@web/AccountLink']")
    SIGN_IN_NAV_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    # def search_product(self):
    #     self.input_text('coffee', *self.SEARCH_FIELD)
    #     self.click(*self.SEARCH_BTN)

    def search_product(self, product):
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)


    # def click_cart(self):
    #     self.click(*self.CART_BTN)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)


    def click_sign_in(self):
        self.wait_and_click(*self.SIGN_IN_BTN)


    def click_sign_in_nav(self):
        self.wait_and_click(*self.SIGN_IN_NAV_BTN)