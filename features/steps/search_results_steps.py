from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Click Add to cart button')
def click_add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click() #always clicks on 1st Add to cart btn
    #content.driver.find_elements(*ADD_TO_CART_BTN)[0].click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME)) # waiting untill the side nav is open
    # SIDE_NAV_PRODUCT_NAME no * cause EC


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart_button(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(6)


@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} not in actual {actual_text}'


@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    url = context.driver.current_url
    assert expected_product in url, f'Expected {expected_product} not in {url}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "") # allow you to execute JS - Force it to scroll down the page and wait
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "") # after scroll to the end of the page

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text # find ele inside this product only not all the page
        assert title, 'Product title not shown' # assert title same as title != '' | search title not equal empty string
        print(title)
        product.find_element(*PRODUCT_IMG)
