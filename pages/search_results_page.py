from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    # def verify_text(self):
    #     actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
    #     assert 'coffee' in actual_text, f'Expected coffee not in actual {actual_text}'

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    # def verify_url(self):
    #     url = self.driver.current_url
    #     assert 'coffee' in url, f'Expected "coffee" not in {url}'

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)


    def add_to_cart_button(self):
        self.click(*self.ADD_TO_CART_BTN)


    def side_nav_add_to_cart_button(self):
        self.click(self.SIDE_NAV_ADD_TO_CART_BTN)


