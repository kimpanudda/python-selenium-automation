from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


@when('Click Add to cart button')
def click_add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(5)


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart_button(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(5)


# @then('Verify search results shown for {expected_product}')
# def verify_search_results(context, expected_product):
#     actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'
#
#
# @then('Verify correct search results URL opens for {expected_product}')
# def verify_url(context, expected_product):
#     url = context.driver.current_url
#     assert expected_product in url, f'Expected {expected_product} not in {url}'
