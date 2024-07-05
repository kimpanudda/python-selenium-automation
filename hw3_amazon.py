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

# find amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-icon a-icon-logo")

# find create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# find your nane
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# find mobile number or email
driver.find_element(By.CSS_SELECTOR, "input[name='email'][type='email']")

# find password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# find password must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, "#auth-password-missing-alert")

# find re-enter password
driver.find_element(By.CSS_SELECTOR, "input[name='passwordCheck'][type='password']")

# find continue
driver.find_element(By.CSS_SELECTOR, "#continue")

# find condition of use
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='register_notification_condition_of_use?']")

# find privacy note
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='register_notification_privacy_notice?']")

# find sign in
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")