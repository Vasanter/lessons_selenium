import os
import time
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

path_to_file = os.path.join(os.getcwd(), "downloads", "gory-voda-nebo-trava.jpg") # директория с файлом
print(f"Директория с файлом: {path_to_file}")

FILE_UPLOAD_FIELD = ('css selector', '#uploadFile')
UPLOADED_FILE_PATH = ('css selector', "#uploadedFilePath")

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")
file_field = driver.find_element(*FILE_UPLOAD_FIELD)
file_field.send_keys(path_to_file)
directory = driver.find_element(*UPLOADED_FILE_PATH)

assert directory.is_displayed() == True, "Директория не найдена!"

time.sleep(5)

print("Тест завершен!")

# driver.quit()  # для FireFox