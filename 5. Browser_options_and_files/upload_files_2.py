import os
from selenium import webdriver

path_to_file = os.path.join(os.getcwd(), "downloads", "gory-voda-nebo-trava.jpg")  # директория с файлом
UPLOAD_BUTTON = ("css selector", "#file-submit")
UPLOAD_FIELD = ('xpath', "//input[@type='file']")
CONFIRM_TEXT = ('xpath', "//h3[contains(text(), 'File Uploaded!')]")

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # используется вместо maximize_window
options.add_argument("--disable-extensions") # отключение плагинов/расширений браузера
options.add_argument('--ignore-certificate-errors') # игнорирование ошибок сертификатов безопасности

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/upload")

# при загрузке файлов используется следующий тип локаторов - //input[@type='file']
upload_field = driver.find_element(*UPLOAD_FIELD)
upload_field.send_keys(path_to_file)

upload_button_click = driver.find_element(*UPLOAD_BUTTON)
upload_button_click.click()

input()

confirm = driver.find_element(*CONFIRM_TEXT)
confirm_text = confirm.text
print(confirm.text)

assert confirm_text == "File Uploaded!", "Файл не загружен!"


print("Тест завершен!")
