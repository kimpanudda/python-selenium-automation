from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class TermsAndConditionsPage(Page):

    TC_PAGE_TITLE_TEXT = (By.XPATH, "//h1[text()='Terms & Conditions']")

    def verify_tc_opened(self):
        self.verify_text('Terms & Conditions', *self.TC_PAGE_TITLE_TEXT)