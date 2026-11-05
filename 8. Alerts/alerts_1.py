import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

BUTTON_ALERT = ("css selector", "#alertButton")

driver.get("https://demoqa.com/alerts")
wait.until(EC.element_to_be_clickable(BUTTON_ALERT)).click()

alert = wait.until(EC.alert_is_present())  # когда алерт (с одной кнопкой) появится он запишется в данную переменную
# переключаемся на алерт
time.sleep(5)
alert.accept() # принимаем условия
time.sleep(5)
print("Тест пройден!")
