import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains  # поможет нам взаимодействовать с мышкой и прочим...
from js_code_for_scrolling.scrolls import Scrolls


# Цепочка действий (Action API) - это довольно-таки низкоуровневая автоматизация (более продвинутая)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)
action = ActionChains(driver)  # создаем объект через который будут выполняться действия мыши
scrolls = Scrolls(driver, action)

"""Пример 1"""
# DOUBLE_CLICK_BUTTON = ('xpath', "//button[@id='doubleClick']")  # 1) Double-Click on button
# LEFT_CLICK_BUTTON = ('xpath', "//button[@id='leftClick']")  # 2) Right-Click on Button
# RIGHT_CLICK_BUTTON = ('xpath', "//button[@id='rightClick']")  # 3) Left-Click on Button
# DISABLE_CLICK_BUTTON = ('xp ath', "//button[@id='disabledButton']")  # 4) Disabled Button
# HOVER_BUTTON = ('xpath', "//button[@id='colorChangeOnHover']")  # 5) Color change on hover button
# NEW_TAB_CLICK_BUTTON = ('xpath', "//button[@id='openNewTab']")  # 6) Click the button to open a link in different window
# NEW_PAGE_CLICK_BUTTON = ('xpath', "//button[@id='loadNewPageInSameTab']")  # 7) Click the button to open a link
# # in same window


# driver.get("https://testkru.com/Elements/Buttons")
# left_button = driver.find_element(*LEFT_CLICK_BUTTON)
# double_button = driver.find_element(*DOUBLE_CLICK_BUTTON)
# right_button = driver.find_element(*RIGHT_CLICK_BUTTON)
# hover_button = driver.find_element(*HOVER_BUTTON)

"""Клик левой кнопкой мыши"""
# action.click(left_button).perform()

"""Двойной клик"""
# action.double_click(double_button).perform()

"""Клик правой кнопкой мыши"""
# action.context_click(right_button).perform()
# action.click(left_button).double_click().context_click().perform()  # цепочка действий

# вызов паузы в цепочке действий
# action.click(left_button).pause(3).double_click(double_button).pause(3).context_click(right_button).pause(3).perform()

"""Наведение на элемент"""
# action.move_to_element(hover_button).perform()  # наведение на элемент


"""Выпадающее меню. Пример 2"""
# driver.get("https://demoqa.com/menu#")

# STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
# STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
# STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")

# STEP_1 = driver.find_element(*STEP_1_LOCATOR)
# STEP_2 = driver.find_element(*STEP_2_LOCATOR)
# STEP_3 = driver.find_element(*STEP_3_LOCATOR)

# цепочка действий с паузами
# action.move_to_element(STEP_1).pause(5) \
#     .move_to_element(STEP_2).pause(5).click(STEP_3).perform()
# time.sleep(5)


"""Скролл к элементу"""
# Для этого у action есть метод scroll_to_element()
# driver.get("https://clipboardjs.com/")
# SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
# SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)
# scrolls.scroll_to_element(SOME_ELEMENT)  # используем скролл до элемента
# time.sleep(5)
