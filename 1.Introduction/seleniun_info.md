# Что такое Selenium WebDriver и как он работает
WebDriver — это API, независимый от языка интерфейс для управления поведением веб-браузеров. 
Каждый браузер поддерживается определенной реализацией WebDriver, называемой драйвером.

Driver — Компонент / сущность, отвечающий за делегирование полномочий браузеру. То есть он обеспечивает коммуникацию между Selenium и браузером, переводя команды, написанные на языке программирования, в формат, понятный браузеру. Он выполняет роль посредника, принимая указания от Selenium Webdriver, передавая их браузеру и возвращая результаты выполнения обратно.

Selenium - это набор инструментов для автоматизации работы с браузерами, в который входят Selenium WebDriver, Selenium IDE и Selenium Grid.


## Создание виртуального окружения
Виртуальное окружение нужно для изоляции проекта, чтобы все устанавливаемые библиотеки использовались только в рамках текущего проекта и не было конфликтов с другими зависимостями.

Первым делом создадим виртуальное окружение:

```bash
python3 -m venv venv
```

В результате, в директории проекта появится папка `venv`.

В команде `python3 -m venv venv` второе `venv` является именем виртуального окружения. Команда разбивается так:
* **`python3`** — вызов интерпретатора Python версии 3.
* **`-m venv`** — указание Python использовать модуль `venv` для создания виртуального окружения.
* **`venv`** — имя каталога, в котором будет создано виртуальное окружение. Это имя является произвольным и может быть заменено на любое другое, которое вы хотите использовать для вашего виртуального окружения.

Теперь необходимо активировать окружение:

### Mac OS:
```bash
source venv/bin/activate
```

### Windows PowerShell:
По умолчанию, в PowerShell может быть включена политика, которая блокирует выполнение скриптов. Чтобы разрешить выполнение скриптов, вам может потребоваться запустить PowerShell от имени администратора и выполнить следующую команду:

```powershell
Set-ExecutionPolicy Unrestricted
```

Далее, перейдите в каталог вашего проекта, где находится виртуальное окружение и активируйте его с помощью команды:

```powershell
venv/Scripts/activate.ps1
```

В результате, в терминале вы увидите префикс с названием окружения примерно такого формата:
```bash
(venv) /НАЗВАНИЕ
```

### Windows CMD:
Перейдите в каталог вашего проекта, где находится виртуальное окружение. Введите следующую команду:
```cmd
.\venv\Scripts\activate
```

> **Важно знать:** окружение работает в рамках текущей сессии окна терминала, т.е если вы закроете терминал, то окружение снова нужно будет активировать.

Но если вы решили удалить папку `venv`, и пересоздать окружение, то сначала деактивируйте его командой:
```bash
deactivate
```

---

## Установка Selenium и зависимостей
После создания и активации тестового окружения в нашем проекте необходимо установить все зависимости (библиотеки) для начала работы.

Первая и самая главная библиотека, это и есть **selenium**. Установка происходит следующим образом:
```bash
pip3 install selenium
```

Обычно этого достаточно, но иногда дополнительно требуется установить библиотеку **packaging**:
```bash
pip3 install packaging
```

> **Заметка:** Ранее использовалась библиотека `webdriver-manager`. Она нужна непосредственно для работы с драйверами Chrome, Firefox и т.д. Но сейчас Selenium выпустил такую вещь, как *Selenium Manager*, и он не нуждается в установке.
>
> Установите его:
```bash
pip3 install webdriver-manager
```

---

## Инициализация Chromedriver
Перед написанием кода, рекомендую обновить Chrome до самой новой версии.

Инициализировать объект драйвера можно одним из предложенных вариантов:

### 1) Инициализация в одну строчку через SeleniumManager
Он автоматически распознает ваш Chrome и запустит его. Но важно перед этим найти у себя на компьютере через поиск `chromedriver.exe` и удалить его!

**Начиная с Selenium 4.6.0 (Selenium 4+)**
Разработчики Selenium встроили собственный менеджер бинарников — **Selenium Manager**. При первом вызове (например, `webdriver.Chrome()` без явного указания пути к chromedriver) Selenium автоматически:
1. Определяет, какие браузеры есть в системе (например, смотрит на реестр в Windows или ищет в стандартных локациях для Linux/macOS).
2. Сравнивает установленную версию браузера (Chrome, Firefox, Edge, Opera, Safari и пр.).
3. Загружает (скачивает) с официального места именно тот драйвер, который точно соответствует версии браузера.
4. Кэширует скачанный бинарник в локальной папке (обычно где-то в профиле пользователя, чтобы не тянуть по сети каждый раз).
5. Запускает браузер через этот уже скачанный (и "подвешенный" в PATH/темповой папке) WebDriver.

Таким образом, вы больше не должны вручную хранить или обновлять `chromedriver.exe` или `geckodriver.exe`: Selenium Manager сделает всё сам "из коробки". Единственное условие — в системе должен быть установлен сам браузер, и он должен нормально открываться.

```python
from selenium import webdriver

driver = webdriver.Chrome()
```

### 2) Инициализация через WebDriverManager
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

### 3) Прямая инициализация WebDriver конкретного браузера
```python
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
```

### 4) Инициализация через WebDriverManager + версия Chrome
*(Но нужно откатывать сам браузер)*
```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager(driver_version="114.0.5735.16").install())
driver = webdriver.Chrome(service=service)
```

Работа Chromedriver бывает не совсем стабильна, поэтому используйте тот вариант, который сработает для вас! Но также держите в голове, что при обновлении Chrome не всегда успевают обновить Chromedriver, и на несколько дней ваш код может перестать работать. Тут может помочь именно webdriver manager.

Отслеживайте проблемы и новости на официальном сайте [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).

---

## Инициализация Firefox
Тут все просто. Используем WebDriverManager либо SeleniumManager, и всё.

### 1) Selenium Manager
```python
from selenium import webdriver

driver = webdriver.Firefox()
```

### 2) WebDriverManager
```python
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Закрываем браузер
driver.quit()
```

---

## driver.close() vs driver.quit()
В Selenium есть два разных способа закрыть браузер, и они делают принципиально разные вещи.

```python
driver.close() # Закрытие одной активной вкладки (если их открыто несколько)
driver.quit()  # Закрывает все окна браузера и полностью завершает текущую сессию
```
