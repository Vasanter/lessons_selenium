# Explicit Wait явное ожидание, чаще используется для ожидания определенного условия, которое должно быть выполнено
# прежде, чем тест пойдет дальше. Ожидание сработает именно там, где оно указано, т.е. есть определенное условие.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # WebDriverWait - отвечает за явное ожидание
from selenium.webdriver.support import expected_conditions as EC  # ожидаемое условие


ENABLE_IN_SECONDS_LOCATOR = ("css selector", "#enableAfter")
VISIBLE_AFTER_LOCATOR = ("css selector", "#visibleAfter")

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 15, poll_frequency=1)  # poll_frequency - определяет то, как часто
# делать новый запрос на проверку выполнения ожидаемого условия. В данном случае 1 секунда

driver.get("https://demoqa.com/dynamic-properties")

enable_is_seconds = wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS_LOCATOR),
                               message="Элемент не кликабилен!")  # ждем пока элемент станет кликабильним
enable_is_seconds.click()

visible_after = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_LOCATOR),
                           message="Элемент не виден!")  # ждем пока один конкретный элемент появится в DOM и станет видимым
visible_after.click()


print("Done!")
