import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://mail.ru/")

"""Добавление Cookies"""
driver.add_cookie({
    "name": "Example",
    "value": "Rabbit"})
print(driver.get_cookie("Example"))  # указываем значение, которое хотим получить

time.sleep(20)

"""Замена Cookies"""
driver.delete_cookie("VID")  # сначала удаляем
driver.add_cookie({"name": "new_domain",
                   "value": "https://www.championat.com/"})  # потом добавляем
time.sleep(20)
print(driver.get_cookies())  # все Cookies

"""Удаление всех Cookies"""
driver.delete_all_cookies()  # удалили все Cookies => []
print(driver.get_cookies())