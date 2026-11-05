import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# ---ПРИМЕР №1---
"""Получение статуса чекбокса через метод get_attribute("checked"), т.е. выставлен чекбокс или нет"""
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

# CHECKBOX = ("xpath", "//input[@id='gdpr_checkbox']")
#
# driver.get("https://www.freeconferencecall.com/global/pl/login")
#
# print(driver.find_element(*CHECKBOX).get_attribute("checked"))  # None
# driver.find_element(*CHECKBOX).click()
# print(type(driver.find_element(*CHECKBOX).get_attribute("checked")))  # true | <class 'str'>

"""Получение статуса чекбокса через метод is_selected()"""
# print(driver.find_element(*CHECKBOX).is_selected())  # is_selected - возвращает либо True либо False
# driver.find_element(*CHECKBOX).click()
# print(driver.find_element(*CHECKBOX).is_selected())
# time.sleep(3)
# print("Все ОК!")


# ---ПРИМЕР №2---
"""Если элемент некликабилен или перекрыт"""
# PLUS_BUTTON = ("xpath", "//span[@class='rc-tree-switcher rc-tree-switcher_close']")
# CHECKBOX_HOME = ("xpath", "//span[@aria-label='Select Home']")
# CHECKBOX_DESKTOP = ("xpath", "//span[@aria-label='Select Desktop']")
#
#
# driver.get("https://demoqa.com/checkbox")
# time.sleep(3)
#
# driver.find_element(*PLUS_BUTTON).click()
#
# print(driver.find_element(*CHECKBOX_DESKTOP).is_selected())
# time.sleep(3)
# driver.find_element(*CHECKBOX_HOME).click()
# time.sleep(3)
# print(driver.find_element(*CHECKBOX_DESKTOP).is_selected())
# print("Все ОК!")


# ---ПРИМЕР №3---
"""Динамические классы"""
# ELEMENT_ONE = ("xpath", "//li[text()='Cras justo odio']")
#
# driver.get("https://demoqa.com/selectable")
# time.sleep(3)
#
# before = driver.find_element(*ELEMENT_ONE).get_attribute("class")  # mt-2 list-group-item list-group-item-action
# print(before)
# before = driver.find_element(*ELEMENT_ONE).click()
# time.sleep(3)
# after = driver.find_element(*ELEMENT_ONE).get_attribute("class")  # mt-2 list-group-item active list-group-item-action
# print(after)
#
# assert "active" in after
# print("Все ОК!")
