from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# find Amazon logo
driver.find_element(By.XPATH,"//*[@class='a-icon a-icon-logo']")

# find Email field
driver.find_element(By.ID,"ap_emai")

# find continue button
driver.find_element(By.ID,"continue")

# find condition of use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")

# find privacy notice link
driver.find_element(By.XPATH,"//*[text()='Privacy Notice']")

# find need help link
driver.find_element(By.XPATH,"//*[text()='Need help?']")

# find forgot your password link
driver.find_element(By.ID,"auth-fpp-link-bottom")
driver.find_element(By.XPATH,"//*[text()='Forgot your password?']")

# find other issue with sign-in
driver.find_element(By.ID,"ap-other-signin-issues-link")
driver.find_element(By.XPATH,"//*[text()='Other issues with Sign-In']")

# find create your amazon account
driver.find_element(By.ID,"createAccountSubmit")
