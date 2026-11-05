from selenium import webdriver

import os  # Модуль для работы с файловой системой и путями
import json  # Модуль для работы с JSON-файлами

class LocalStorage:
    def __init__(self, driver):
        # Конструктор класса принимает объект драйвера браузера и сохраняет его как атрибут
        self.driver = driver
        # Путь к директории для хранения файлов Local Storage
        self.storage_path = os.path.join(os.getcwd(), "local-storage")

    def _get_storage(self):
        # Внутренний метод для получения всех данных из Local Storage
        return self.driver.execute_script(
            """
            let items = {};  // Объект для хранения ключей и значений
            for (let i = 0; i < localStorage.length; i++) {
                let key = localStorage.key(i);  // Получение ключа по индексу
                items[key] = localStorage.getItem(key);  // Получение значения по ключу
            }
            return items;  // Возврат всех элементов Local Storage
            """
        )

    def _get_file_path(self, filename: str) -> str:
        """Вспомогательный метод для генерации пути к файлу на основе имени файла."""
        return os.path.join(self.storage_path, f"login-{filename}.json")

    def save(self, filename: str = "main"):
        # Метод для сохранения данных Local Storage в файл
        local_storage = self._get_storage()  # Получение данных Local Storage
        if not local_storage:
            # Если данных нет, вызывается исключение
            raise ValueError("Нет данных в Local Storage для сохранения.")

        file_path = self._get_file_path(filename)  # Генерация пути к файлу
        os.makedirs(self.storage_path, exist_ok=True)  # Создание директории, если её нет
        try:
            with open(file_path, "w") as file:
                json.dump(local_storage, file)  # Запись данных в JSON-файл
            print(f"Данные Local Storage успешно сохранены в {file_path}.")
        except (OSError, IOError) as e:
            # Обработка ошибок при записи в файл
            print(f"Ошибка при сохранении данных Local Storage: {e}")

    def load(self, filename: str = "main"):
        # Метод для загрузки данных из файла в Local Storage
        file_path = self._get_file_path(filename)  # Генерация пути к файлу
        if not os.path.exists(file_path):
            # Если файл не существует, выводится сообщение
            print(f"Файл {file_path} не существует.")
            return

        try:
            with open(file_path, "r") as file:
                storage_data = json.load(file)  # Загрузка данных из JSON-файла

            for key, value in storage_data.items():
                # Добавление данных в Local Storage с помощью JavaScript
                self.driver.execute_script("localStorage.setItem(arguments[0], arguments[1]);", key, value)
            self.driver.refresh()  # Обновление страницы после загрузки данных
            print(f"Данные Local Storage успешно загружены из {file_path}.")
        except (OSError, IOError, json.JSONDecodeError) as e:
            # Обработка ошибок при чтении данных из файла
            print(f"Ошибка при загрузке данных Local Storage: {e}")