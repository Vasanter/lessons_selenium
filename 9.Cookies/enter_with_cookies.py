import os
from selenium import webdriver
from cookie_manager import CookieManager

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
GDPR_CHECKBOX = ("xpath", "//input[@id='gdpr_checkbox']")
SUBMIX_BUTTON = ("xpath", "//button[@id='loginformsubmit']")


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
cookie_manager = CookieManager(driver)

driver.get("https://www.freeconferencecall.com/global/pl/login")

if os.path.exists("cookies.json"):
    # Создаем экземпляр класса и передаем в него наш driver
    cookie_manager.load()
else:
    driver.find_element(*LOGIN_FIELD).send_keys("vkmorozov@wydevoice.com")
    driver.find_element(*PASSWORD_FIELD).send_keys("123")
    driver.find_element(*GDPR_CHECKBOX).click()
    driver.find_element(*SUBMIX_BUTTON).click()
    cookie_manager.save()