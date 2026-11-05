import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

PROMPT_ALERT_BUTTON = ("css selector", "#promtButton")
SELECTED_ACCEPT = ('css selector', "#promptResult")

wait.until(EC.element_to_be_clickable(PROMPT_ALERT_BUTTON)).click()
alert = wait.until(EC.alert_is_present())

alert.send_keys("Vladimir")
time.sleep(5)
alert.accept()  # принимаем условия
time.sleep(5)
selected_accept = driver.find_element(*SELECTED_ACCEPT)
print(selected_accept.text)

# """В случае если система запрашивает логин/пароль"""
# # driver.get('https://<username>:<password>@<site-needing-auth>.com')
# # alert = driver.switch_to_alert()
# # alert.accept()


