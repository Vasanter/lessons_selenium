from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)  # !!!
wait = WebDriverWait(driver, 10, poll_frequency=1)

FORM_NAME_FIELD_LOCATOR = ('xpath', "//*[@id='RESULT_TextField-0']")  # элемент внутри iframe
COPY_TEXT_LOCATOR = ('xpath', "//*[text()='Copy Text']")  # элемент вне iframe

# driver.get("https://the-internet.herokuapp.com/nested_frames")
#
# driver.switch_to.frame(1)  # передаем id фрейма и переключаемся на него
# print(driver.find_element('xpath', "//body[contains(.,'BOTTOM')]").text)

"""Вложенные iframes"""

# driver.get("https://demoqa.com/nestedframes")
#
# driver.switch_to.frame("frame1")
# print(driver.find_element("xpath", "//body").text)
#
# driver.switch_to.frame(0)  # 0 - индекс
# print(driver.find_element("xpath", "//body").text)

"""Переключение на родительский iframe"""
# driver.switch_to.parent_frame()
# print(driver.find_element("xpath", "//body").text)


"""Возврат на дефолтный контент"""
# driver.switch_to.default_content()  # перейдем к главному контенту страницы
# driver.find_element(*COPY_TEXT_LOCATOR).click()
# time.sleep(5)
# print("Все ОК!")