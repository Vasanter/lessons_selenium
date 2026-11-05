import json
from selenium import webdriver
from cookie_manager import CookieManager

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
cookie_manager = CookieManager(driver)


# ИСПОЛЬЗУЕМ CookieManager!
driver.get("https://www.freeconferencecall.com/global/pl/login")
# Создаем экземпляр класса и передаем в него наш driver
cookie_manager.save()  # используем CookieManager


# driver.get("https://www.freeconferencecall.com/global/pl/login")
#
# # Авторизуемся и жмем Enter
# input()
#
# cookies = driver.get_cookies()
#
# with open("cookies.json", "w") as file:
#     json.dump(cookies, file, indent=4)
#
# print("Done!")
