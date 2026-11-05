import functools
import time
from selenium import webdriver


def decorator(func):
    @functools.wraps(func)  # Используем для сохранения метаданных оригинальной функции
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            # Выполняем функцию и сразу возвращаем её результат, если всё успешно
            result = func(*args, **kwargs)
            return result
        finally:
            # Блок finally выполнится даже если func() вызовет ошибку
            end_time = time.perf_counter()
            print(f"Время выполнения: {(end_time - start_time):.2f} сек.")

    return wrapper


@decorator
def run_my_test():
    driver = webdriver.Chrome()  # Инициализация драйвера
    try:
        driver.maximize_window()
        driver.get("https://vk.com")  # Переход на страницу
        assert driver.title == "ВКонтакте | Добро пожаловать", f"Титульная страница называется: {driver.title}"
        print("Сессия завершена!")
    finally:
        # Браузер закроется в любом случае: даже если assert упадет
        driver.quit()


# Запуск функции
run_my_test()