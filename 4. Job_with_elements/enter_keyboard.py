import platform
from selenium import webdriver
from selenium.webdriver import Keys

print(f"Твоя система: {platform.system()}")
# в зависимости от системы будет нажата кнопка COMMAND или CONTROL
CMD_CTRL = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL


driver = webdriver.Chrome()
driver.maximize_window()


KEYBOARD_INPUT = ("xpath", "//input[@id='target']")

driver.get("https://the-internet.herokuapp.com/key_presses")

driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.PAUSE)
input()
driver.find_element(*KEYBOARD_INPUT).send_keys("HOLLAND")
input()
driver.find_element(*KEYBOARD_INPUT).send_keys(CMD_CTRL + "A")  # выделяем весь текст
input()
driver.find_element(*KEYBOARD_INPUT).send_keys(Keys.BACKSPACE)  # очищаем поле | альтернатива clear
print("DONE!")
