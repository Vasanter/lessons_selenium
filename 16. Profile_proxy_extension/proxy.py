import random
import time
from seleniumwire import webdriver

# Список прокси: (host, port, username, password)
proxies = [
    ("150.241.251.155", 51523, "login", "password"),
    ("94.131.56.182", 51523, "login", "password"),
    ("2.59.60.128", 51523, "login", "password"),
    # ... добавь остальные
]

# Выбираем случайный прокси
proxy_host, proxy_port, proxy_user, proxy_pass = random.choice(proxies)

# Настраиваем selenium-wire
proxy_options = {
    'proxy': {
        'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
        'https': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
        # SOCKS? → 'socks5://user:pass@host:port'
    }
}

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')  # если прокси лезет в TLS

# Запуск браузера
driver = webdriver.Chrome(seleniumwire_options=proxy_options, options=options)

# Проверим IP
driver.get("https://httpbin.org/ip")
time.sleep(5)

driver.quit()