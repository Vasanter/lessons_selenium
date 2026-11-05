import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

class DatePickerHandler:

    _DATEPICKER_TRIGGER_BUTTON = ("xpath", "//div[@data-id='top-header.avia.search-form.segment.calendar-from']")  # поле выбора даты
    _DATEPICKER = ("xpath", "//div[@data-mode='range']")  # окно с календарем
    _CALENDAR_MONTH_AND_YEAR = ("xpath", ".//table[@role='grid']")  # левый блок календаря, где отображается месяц/год
    _NEXT_MONTH_BUTTON = ("css selector", ".rdp-button_next")  # кнопка следующего месяца
    _DAY_LOCATOR = ("xpath", ".//td[@class='rdp-day']")  # день

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        # Инициализируем объект WebDriverWait с таймаутом 30 секунд для надежности
        self.wait = WebDriverWait(driver, 30)

    def _get_datepicker(self) -> WebElement:
        """Ждет появления и возвращает элемент календаря."""
        return self.wait.until(EC.visibility_of_element_located(self._DATEPICKER))

    def open(self):
        """Открывает календарь, кликая по триггерной кнопке с ожиданием."""
        print("-> Открытие календаря...")
        # Ждем, пока триггерная кнопка станет кликабельной и нажмем ее.
        trigger_button = self.wait.until(EC.element_to_be_clickable(self._DATEPICKER_TRIGGER_BUTTON))
        trigger_button.click()

    def _go_to_month(self, month: int, year: int):
        """Навигирует календарь к указанному месяцу и году с использованием явных ожиданий."""
        datepicker = self._get_datepicker()
        target_month_year = f"{MONTHS[month]} {year}"

        print(f"-> Навигация в месяц: {target_month_year}...")
        
        # Создаем функцию-проверку, которая будет передана WebDriverWait.
        def check_month_in_header(driver):
            try:
                calendar_header = driver.find_element(*self._CALENDAR_MONTH_AND_YEAR)
                return target_month_year in calendar_header.text
            except Exception:
                # Возвращаем False, если что-то пошло не так с поиском элемента
                return False

        try:
            # Ждем, пока заголовок календаря НЕ станет содержать нужный месяц/год. 
            # Если он уже содержит, условие пройдет мгновенно (или через минимальное время ожидания).
            self.wait.until(check_month_in_header)
        except Exception as e:
            print(f"Не удалось дойти до месяца {target_month_year} за отведенное время.")
            raise

    def _select_day(self, day: int):
        """Находит и кликает элемент дня с использованием XPath по тексту."""
        datepicker = self._get_datepicker()
        print(f"-> Выбор даты: {day}")
        
        # Создаем максимально точный XPath для конкретного дня. 
        # Использование text() в XPath - самый надежный способ найти элемент по его видимому содержимому.
        day_xpath = f".//td[normalize-space(text())='{day:d}']"

        try:
            # Ждем, пока такой день станет кликабельным и нажимаем его.
            day_element = self.wait.until(EC.element_to_be_clickable((self._DAY_LOCATOR + "," + day_xpath)))
            day_element.click()
        except Exception as e:
             print(f"!!! Ошибка при выборе дня {day}. Возможно, календарь еще не обновился или элемент не найден. Причина: {e}")
             raise

    def _set_date_in_month(self, day: int, month: int, year: int):
        """Устанавливает дату в заданном месяце и году."""
        # 1. Навигация к правильному месяцу/году (это вызывает клики на стрелку "Вперед")
        self._go_to_month(month, year)
        # 2. Клик по дате
        self._select_day(day)

    def set_dates(self, from_date: tuple[int, int, int], to_date: tuple[int, int, int]):
        """Устанавливает диапазон дат (от и до)."""
        print("--- Начинаем установку диапазона дат ---")
        # Устанавливаем начальную дату
        self._set_date_in_month(*from_date) 
        
        # Если даты разные, устанавливаем конечную дату.
        if from_date != to_date:
             print("Устанавливаем вторую (конечную) дату...")
             self._set_date_in_month(*to_date)
        else:
             print("Начальная и конечная даты совпадают, дополнительный вызов не требуется.")