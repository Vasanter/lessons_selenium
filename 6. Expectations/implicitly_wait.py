from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # используется вместо maximize_window
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demoqa.com/dynamic-properties")
driver.implicitly_wait(10)  # неявное ожидание - драйвер будет спрашивать страницу в течении 10 сек о наличии элемента

VISIBLE_AFTER_BUTTON = ("css selector", "#visibleAfter")

driver.find_element(*VISIBLE_AFTER_BUTTON).click()

# Неявное ожидание - это количество времени (которое указывается нами) в течение которого, WebDriver
# будет опрашивать DOM. Неявным оно называется, так как мы не указываем чего ждать, изменения текста, размера и т.д…
# Как мы знаем, появление элемента в DOM, не значит, что он появился визуально, т.е обладает высотой, шириной и т.д в
# общем пользователь его может и не видеть.

# Важно знать:
# ➖ Указывается 1 раз в коде и работает для всей сессии.
# ➖ В основном применяется для find_element() и find_elements(), потому что как раз эти методы запрашивают обновления
# элемента на странице.
# ➖ При проверке на исчезновение элемента будет задерживать наши тесты.
