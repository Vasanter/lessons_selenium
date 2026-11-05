import time
from selenium import webdriver
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)


"""Пример 1"""
# driver.get("https://demoqa.com/select-menu")
#
# driver.find_element("xpath", "//div[@id='withOptGroup']").click()  # dropdown Select Value
#
#
# # Функция для выбора элемента по тексту
# def choose_dropdown_element_by_text(text):
#     elements = driver.find_elements("xpath", "//div[@role='option']")
#     for elem_name in elements:
#         if text in elem_name.text:
#             return elem_name
#
#
# # Выбор нужной опции и клик
# choose_dropdown_element_by_text("Another root option").click()
# time.sleep(3)
# print("Выбрано:", driver.find_element("xpath", "//div[@id='withOptGroup']").text)

# setTimeout(function() { debugger; }, 5000);  -- для инспектирования страницы


"""Пример 2"""
# driver.get("https://demoqa.com/select-menu")
#
# MULTISELECT = ("xpath", "(//input[@role='combobox'])[3]")  # dropdown Multiselect drop down
# driver.find_element(*MULTISELECT).click()
#
# select = driver.find_element(*MULTISELECT)
#
# def choose_elem(text):
#     select.send_keys(text)
#     time.sleep(2)
#     select.send_keys(Keys.ENTER)
#     time.sleep(2)
#     select.send_keys(Keys.ESCAPE)
#     time.sleep(2)
#
# choose_elem("Black")
# choose_elem("Green")
