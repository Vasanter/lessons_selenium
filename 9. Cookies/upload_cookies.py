import json
import time
from selenium import webdriver
from cookie_manager import CookieManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
cookie_manager = CookieManager(driver)

# ИСПОЛЬЗУЕМ CookieManager!
# driver.get("https://www.freeconferencecall.com/global/pl/login")
# cookie_manager.load()  # используем CookieManager


# предварительно выполнен скрипт из saves_cookies.py
driver.get("https://www.freeconferencecall.com/global/pl/login")
driver.delete_all_cookies()

input()

with open("cookies.json", "r") as file:
    cookies = json.load(file)

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(3)
driver.quit()
