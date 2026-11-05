import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--ignore-certificate-errors')
# убираем внутренний флаг браузера, который сообщает сайтам, что управление движком перехвачено автоматическим скриптом
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# отключаем вывод уведомления вверху экрана: «Браузером Chrome управляет автоматизированное тестовое ПО»
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# запрещаем Chrome загружать внутреннее расширение автоматизации, которое Selenium использует для некоторых служебных команд
chrome_options.add_experimental_option("useAutomationExtension", False)
# подменяем стандартную строку User-Agent браузера на строку обычного пользователя
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.230 Yowser/2.5 Safari/537.36")


driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)


driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
time.sleep(5)

# driver.save_screenshot("screen.png")  # делаем скриншот, см. WebDriver(New) =	present (failed) / missing (passed)
