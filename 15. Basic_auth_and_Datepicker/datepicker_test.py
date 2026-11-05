import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datepicker_handler import DatePickerHandler
from selenium.common.exceptions import NoSuchElementException, TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, 1)
datepicker = DatePickerHandler(driver)

ACCEPT_COOKIES = ("xpath", "//div[.='Принять']")

driver.get("https://www.aviakassa.com/routes/from-moscow")

time.sleep(5)

# try:
#     wait.until(EC.element_to_be_clickable(ACCEPT_COOKIES)).click()
# except TimeoutException as error:
#     ...
# except NoSuchElementException as error:
#     ...

datepicker.open()

datepicker.set_dates((1, 1, 2027), (2, 2, 2027))
time.sleep(3)