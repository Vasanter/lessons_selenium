import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # WebDriverWait - отвечает за явное ожидание
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

ENABLE_BUTTON_LOCATOR = ("xpath", "//button[text()='Enable']")
TEXT_FIELD_LOCATOR = ("xpath", "//*[@id='input-example']//input[1]")
ENABLE_TEXT_LOCATOR = ("id", "message")

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON_LOCATOR)).click()  # ожидаем что элемент кликабилен
wait.until(EC.element_to_be_clickable(TEXT_FIELD_LOCATOR)).send_keys("HELLO!")
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD_LOCATOR, "HELLO!"))  # приостанавливает выполнение теста и
# ждет (до истечения тайм-аута), пока в свойстве value искомого элемента не появится заданная строка
time.sleep(5)

enabled = driver.find_element(*ENABLE_TEXT_LOCATOR)
enabled_text = enabled.text
print(enabled_text)  # It's enabled!

disable = driver.find_element("xpath", "//button[text()='Disable']")
disable_text = disable.text
assert  disable_text == "Disable", "Элемент не заблокирован!"
