import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

"""ПРИМЕР 1"""

# # Шаг 1 - Открыть базовую страницу
# driver.get("https://whatismyipaddress.com/")
#
# # Шаг 2 - Открытие нескольких вкладок
# driver.switch_to.new_window("tab")
# driver.switch_to.new_window("tab")
# time.sleep(2)
#
# # Шаг 3 - Получение списка всех открытых вкладок
# windows = driver.window_handles
# print(f"Кол-во открытых вкладок: {len(windows)}")
# print("Дескрипторы вкладок: ", windows)
#
# # Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
# current_tab = driver.current_window_handle
# print("Дескриптор текущей вкладки: ", current_tab)
# print("Индекс текущей вкладки:", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности
#
# # Шаг 5 - Переключение на вкладку по ее индексу
# driver.switch_to.window(windows[1])
# time.sleep(2)
# new_current_window = driver.current_window_handle
# new_current_tab = driver.current_window_handle
# print(f"Индекс и дескриптор после переключения: {driver.window_handles.index(new_current_window)} - {new_current_tab}")
#
# # Шаг 6 - Проверка, что вкладка переключилась
# assert current_tab != driver.current_window_handle, "Вкладка не переключилась"


"""ПРИМЕР 2"""

# driver.get("https://the-internet.herokuapp.com/windows")
#
# original_tab = driver.current_window_handle  # сохраняем дескриптор текущей вкладки
# tab_count = len(driver.window_handles)  # считаем количество открытых окон
# assert tab_count == 1
#
# #  находим на странице ссылку и кликаем по ней, что провоцирует открытие новой вкладки в браузере
# driver.find_element("xpath", "//div[@class='example']//a").click()
#
# # программа приостанавливает выполнение и ждет, пока количество окон в браузере не станет равным двум (текущее количество + 1)
# wait.until(EC.number_of_windows_to_be(tab_count + 1))
#
#
# for window_handle in driver.window_handles: # перебираем все доступные окна
#     if window_handle != original_tab:  # ищем то окно, идентификатор которого не равен нашей первой (оригинальной) вкладке
#         driver.switch_to.window(window_handle)  # как только такое окно найдено, фокус переключается на него
#         break
#
# # ищем элемент (заголовок с текстом "New Window") уже внутри новой вкладки и кликаем по нему
# driver.find_element("xpath", "//div[@class='example']/h3[text()='New Window']").click()