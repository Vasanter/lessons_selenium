from selenium import webdriver


with webdriver.Chrome() as driver:  # можно использовать контекстный менеджер для закрытия сессии в браузере
    driver.maximize_window()
    driver.get("https://vk.ru/")
    first_title = driver.title  # получение заголовка страницы
    print(f'URL: {driver.current_url}')  # получение url страницы
    assert first_title == "ВКонтакте | Добро пожаловать", f"Название титульной страницы: {first_title}"

    driver.find_element('xpath', "//span[contains(text(), 'Создать аккаунт')]").click()

    print("Жми Enter в консоли!")
    input()  # для отладки можно использовать input вместо time.sleep, просто нажимая Enter в консоли
    driver.refresh()  # обновление страницы
    print("Произошло обновление страницы")
    input()
    driver.back()  # кнопка "Назад" в браузере
    print("Вернулись назад")
    input()
    driver.forward()  # кнопка "Вперед" в браузере
    print("Вернулись вперед")
    input()
    last_title = driver.title
    print(f"Тест пройден! Заголовок последней страницы на которой ты был: '{last_title}'")
