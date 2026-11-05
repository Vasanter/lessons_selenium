import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

CONFIRM_ALERT = ("css selector", "#confirmButton")
wait.until(EC.element_to_be_clickable(CONFIRM_ALERT)).click()

alert = wait.until(EC.alert_is_present())  # когда алерт (с двумя кнопками) появится, то он запишется в данную переменную
# отклоняем условия
alert.dismiss()
selected_cancel = driver.find_element('css selector', "#confirmResult")
print(selected_cancel.text)


wait.until(EC.element_to_be_clickable(CONFIRM_ALERT)).click()
# принимаем условия
alert.accept()
selected_accept = driver.find_element('css selector', "#confirmResult")
print(selected_accept.text)


