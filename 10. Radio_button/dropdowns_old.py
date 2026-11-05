import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

time.sleep(5)
driver.get("https://the-internet.herokuapp.com/dropdown")

DROPDOWN_ELEMENT = Select(driver.find_element(*SELECT_LOCATOR))  # Select нужен для взаимодействия с элементами внутри локатора
time.sleep(3)

"""Пример 1: Взаимодействие с dropdown по тексту"""
# DROPDOWN_ELEMENT.select_by_visible_text("Option 1")
# time.sleep(3)


"""Пример 2: Взаимодействие с dropdown используя value"""
# DROPDOWN_ELEMENT.select_by_value("1")
# time.sleep(3)


"""Пример 3: Взаимодействие с dropdown используя index"""
# DROPDOWN_ELEMENT.select_by_index(2)
# time.sleep(3)


"""Перебор элементов в dropdown по тексту"""
# all_options = DROPDOWN_ELEMENT.options
# print(all_options)  # получим список веб элементов
#
# for option in all_options:
#     time.sleep(3)
#     if "Option 2" in option.text:  # проверка наличия элемента
#         print("Option 2 - присутствует")
#
#     DROPDOWN_ELEMENT.select_by_visible_text(option.text)  # перебор по тексту
#     time.sleep(3)


"""Перебор элементов в dropdown по индексу"""
# all_options = DROPDOWN_ELEMENT.options
#
# for option in all_options:
#     DROPDOWN_ELEMENT.select_by_index(all_options.index(option))  # перебор по индесу
#     time.sleep(3)


"""Перебор элементов в dropdown по value"""
# # 1. Сначала просто собираем все значения value в текстовый список
# all_values = [opt.get_attribute("value") for opt in DROPDOWN_ELEMENT.options]
#
# # 2. Перебираем сохраненные строки (это не вызовет ошибку устаревшего элемента)
# for value in all_values:
#     if value: # проверка на случай, если у первой опции (например, "Выберите элемент") value пустой
#         DROPDOWN_ELEMENT.select_by_value(value)
#         print(value)
#         time.sleep(3)

