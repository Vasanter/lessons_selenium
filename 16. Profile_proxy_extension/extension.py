import time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_extension(r'C:\Automation\lessons_selenium\extentions_app\ublock-crx\ublock.crx')  # Указываем путь к расширению

driver = webdriver.Chrome(options=options)

# Открываем тестовую страницу
driver.get("https://demo.guru99.com/test/newtours/")
time.sleep(10)