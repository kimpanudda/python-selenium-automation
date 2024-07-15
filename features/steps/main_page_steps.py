from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(2)



@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)
#
#
# @when('Click on cart icon')
# def click_cart_icon(context):
#     context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click() #(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
#     sleep(3)
#
#
# @then('Verify header in shown')
# def verify_header_present(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")
#
#
# @then('Verify header has {number} links')
# def verify_header_link_amount(context, number):
#     number = int(number)  # convert str "6" ==> to int 6
#     links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
#     assert len(links) == number, f'Expected {number} links but got {len(links)}'
#
#     # Make sure to always assert len() for multiple elements as shown above
#     # because .find_elements() function never fails.
#     # This code with incorrect locator will always pass:
#     # context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav2613542']")


@when('Click on Target Circle link')
def click_target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-circleCardLI").click()
    # context.driver.execute_script("window.scrollBy(0, 810)")
    sleep(5)


@then('Verify benefit cells has {number} links')
def verify_benefit_cells_amount(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='CellsComponent/Link'] h3")
    print(links)
    assert len(links) == number, f'Expected {number} links but got {len(links)}'





