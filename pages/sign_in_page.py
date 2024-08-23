from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_TXT = (By.XPATH, "//h1//span")


    def verify_sign_in_opened(self):
        expected_text = 'Sign into your Target account'
        actual_text = self.driver.find_element(*self.SIGN_IN_TXT).text
        assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

