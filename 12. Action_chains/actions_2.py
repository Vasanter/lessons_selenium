import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains  # поможет нам взаимодействовать с мышкой и прочим...
from selenium.webdriver.support import expected_conditions as EC

# Цепочка действий (Action API) - это довольно-таки низко-уровнивая автоматизация (более продвинутая)

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)  # !!!
wait = WebDriverWait(driver, 15, poll_frequency=1)
action = ActionChains(driver)


"""Перетаскивание. Пример 1"""
# driver.get("https://demoqa.com/droppable")
#
# SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
# TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")
#
# SOURCE = driver.find_element(*SOURCE_LOCATOR)
# TARGET = driver.find_element(*TARGET_LOCATOR)
#
# wait.until(EC.element_to_be_clickable(SOURCE))
# action.drag_and_drop(SOURCE, TARGET).perform() # перетаскивание
# time.sleep(3)


"""Перетаскивание. Пример 2"""
driver.get("https://demoqa.com/sortable")

SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")

# функция для указания заменяемых элементов
# def drag_and_drop(source: int, target: int):
#     elements = driver.find_elements("xpath", "//div[@class='list-group']/div")
#     source_element = elements[source - 1]
#     target_element = elements[target - 1]
#     wait.until(EC.element_to_be_clickable(source_element))
#     action.drag_and_drop(source_element, target_element).perform()
#
# drag_and_drop(5, 2)
#
# time.sleep(10)


"""Отпускание кнопки мыши. Пример 3"""
# driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")
#
# source = driver.find_element("xpath", "//div[@class='grid__item'][7]") # что перетаскиваем
# target = driver.find_element("xpath", "//div[@class='drop-area__item'][2]") # куда перетаскиваем
#
# action.click_and_hold(source).pause(3) \
#     .move_to_element(target).release() \
#     .perform()