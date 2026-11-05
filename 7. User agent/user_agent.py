import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--ignore-certificate-errors')
# User agent – содержащая в себе информацию о клиенте строка, т.е это некий идентификатор,
# который позволяет браузеру идентифицировать нас, как пользователя.
chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) //"
                            " AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1")
# указываем User Agent / гугли: user agent list

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
driver.get("https://vk.com/")
time.sleep(5)

# driver.save_screenshot("screen.png")  # делаем скриншот, см. WebDriver(New) =	present (failed) / missing (passed)
