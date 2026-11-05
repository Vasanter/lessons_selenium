import os
import time
from selenium import webdriver

path_to_file = os.path.join(os.getcwd(), "downloads", "gory-voda-nebo-trava.jpg")  # директория с файлом
DOWNLOAD_BUTTON = ("css selector", "#downloadButton")


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # используется вместо maximize_window
options.add_argument("--disable-extensions") # отключение плагинов/расширений браузера
options.add_argument('--ignore-certificate-errors') # игнорирование ошибок сертификатов безопасности
# задаем директорию для загружаемых файлов
preferences = {
    "download.default_directory": os.path.join(os.getcwd(), "downloads"),
    "safebrowsing.enabled" : True,  # отключает проверку "нежелательное ПО"
    "download.prompt_for_download" : False, # отключает запрос-подтверждение при скачивании файла
    "download.directory_ypgrade" : True,  # указывает браузеру, что необходимо автоматически обновить дефолтную
    # директорию загрузки до указанной вами новой папки
}
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/upload-download")
driver.find_element(*DOWNLOAD_BUTTON).click()

time.sleep(5)
assert os.path.exists(os.path.join(os.getcwd(), "downloads", "sampleFile.jpeg")) == True, "Файл не найден!"

print("Тест завершен!")
