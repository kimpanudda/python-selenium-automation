from selenium.webdriver.common.by import By
from behave import when, then




@when('Click on the Sign in button')
def click_on_sign_in_button(context):
    context.app.header.click_sign_in()


@then('Click on the Sign in button in the right side nav menu')
def click_on_sign_in_nav_menu(context):
    context.app.header.click_sign_in_nav()


@then('Sign in form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_opened()


