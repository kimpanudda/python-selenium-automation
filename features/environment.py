from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application


def browser_init(context): #start browserb
    """
    :param context: Behave context
    """
    driver_path = './chromedriver'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service) #it store in Behave 'context' that why we use context

    context.driver.maximize_window() #full screen
    context.driver.implicitly_wait(4) #checks for Element every 100ms
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario): #default
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature): #after scenario
    context.driver.quit()
