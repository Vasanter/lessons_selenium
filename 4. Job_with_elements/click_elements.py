import time
from selenium import webdriver

WIKI_SEARCH_FIELD = ("css selector", ".wikipedia-search-input")
BUTTON_FIELD = ("xpath", "//input[@type='submit']")
TEXT_ERROR = ('xpath', "//div[text()='Please enter text to search.']")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
search_button = driver.find_element(*BUTTON_FIELD)  # кнопка поиска
search_button.click()

time.sleep(3)
alert = driver.find_element(*TEXT_ERROR)
alert_text = alert.text
print(f"Алерт об отсутствии текста для поиска: '{alert_text}'")

assert alert_text == "Please enter text to search.", "Алерт отсутствует!"

wikipedia_search_input = driver.find_element(*WIKI_SEARCH_FIELD)
wikipedia_search_input.send_keys("Nikola Tesla")
time.sleep(3)

print(wikipedia_search_input.get_attribute("value"))  # используя value мы можем получить значение из поля | Nikola Tesla
print(wikipedia_search_input.get_attribute("id"))  # Wikipedia1_wikipedia-search-input
print(wikipedia_search_input.get_attribute("href"))  # None
search_button.click()

time.sleep(3)
search_100_metres = driver.find_element("xpath", "//a[.='Nikola Tesla']")
search_100_metres_text = search_100_metres.text

assert search_100_metres_text == "Nikola Tesla", "Ожидаемый результат не найден!"

wikipedia_search_input.clear()  # очищаем поле от введенных данных
wikipedia_search_input.send_keys("Serbia")
search_button.click()
time.sleep(3)

search_serbia = driver.find_element("link text", "Serbia")
search_serbia_text = search_serbia.text

assert search_serbia_text == "Serbia", "Не найден результат при поиске!"


print("Тест закончен!")
