from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def search_product(context):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)


@then('Verify search worked')
def verify_search_results(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(3)


@then('Verify cart is empty')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div//h1").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'


@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(6)


@when('Click sign in from right side')
def click_sign_in_right(context):
    context.driver.find_element(By.CSS_SELECTOR, "#listaccountNav-signIn").click()
    sleep(6)


@then('Verify sign in form opened')
def verify_sign_in_form(context):
    expected_text = "Sign into your Target account"
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_text in actual_text, f'Expected {expected_text} but got {actual_text}'

    # expected_form = context.driver.find_element(By.XPATH, "//div[@data-test='@web/auth-components/AuthSignInFlyout']")
    # assert expected_form.is_displayed(), f'Sign in form is not displayed'

    print("Test passed")


