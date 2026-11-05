import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

# ---ПРИМЕР №1---
RADIO_YES_STATUS = ("xpath", "//input[@id='yesRadio']")
RADIO_YES_ACTION = ("xpath", "//label[@for='yesRadio']")

RADIO_IMPRESSIVE = ("xpath", "//input[@id='impressiveRadio']")
RADIO_IMPRESSIVE_ACTION = ("xpath", "//label[@for='impressiveRadio']")

RADIO_NO_STATUS = ("xpath", "//label[@id='noRadio']")
RADIO_NO_ACTION = ("xpath", "//label[@for='noRadio']")


driver.get("https://demoqa.com/radio-button")
time.sleep(3)

# --- Пример 1---
"""Выбираем radio-button"""
print(driver.find_element(*RADIO_YES_STATUS).is_selected())  # False
driver.find_element(*RADIO_YES_ACTION).click()
print(driver.find_element(*RADIO_YES_STATUS).is_selected())  # True
time.sleep(3)

# --- Пример 2: Проверяем что элемент заблокирован---
"""radio-button  => is_enabled"""
print(driver.find_element(*RADIO_NO_ACTION).is_enabled())  # проверяем что данная кнопка доступна для взаимодействия
