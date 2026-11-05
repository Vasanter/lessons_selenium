from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


REMOVE_BUTTON_LOCATOR = ("xpath", "//button[.='Remove']")
BUTTON_GONE_LOCATOR = ('css selector', "#message")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 15, poll_frequency=1)  # poll_frequency - как часто мы опрашиваем страницу
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

driver.find_element(*REMOVE_BUTTON_LOCATOR).click()
print(wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON_LOCATOR)))  # ожидаем исчезновение элемента | True

button_gone = driver.find_element(*BUTTON_GONE_LOCATOR)
button_gone_text = button_gone.text
print(button_gone_text)  # It's gone!
