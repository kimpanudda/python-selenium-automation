from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')



@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Actual product in cart name: {actual_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify cart is empty')
def verify_cart_empty(context):
    # expected_text = 'Your cart is empty'
    # actual_text = context.driver.find_element(By.XPATH, "//div//h1").text #(By.CSS_SELECTOR, "[@data-test='boxEmptyMsg'] h1")
    # print(actual_text)
    # assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    context.app.cart_page.verify_cart_empty()