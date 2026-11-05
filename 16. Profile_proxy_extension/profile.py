import shutil
import tempfile
import time
import os
import platform
from selenium import webdriver

os_name = platform.system()
username = input("Enter profile name: ")

# Формирование пути к профилю в зависимости от ОС
if os_name == "Darwin":
    chrome_profiles_root = f"/Users/{username}/Library/Application Support/Google/Chrome"
elif os_name == "Windows":
    chrome_profiles_root = rf"C:\Users\{username}\AppData\Local\Google\Chrome\User Data"
else:
    chrome_profiles_root = f"/home/{username}/.config/google-chrome"

# Путь к директории профиля
profile_directory = "Profile 1"

# Полный путь до профиля
original_profile_path = os.path.join(chrome_profiles_root, profile_directory)

# Проверка существования директории профиля
if not os.path.exists(original_profile_path):
    raise Exception("Profile directory doesn't exists")

# Копируем профиль во временную директорию
temp_user_data_dir = tempfile.mkdtemp()


def _copy_ignore_locked(src, dst):
    """Копирует файл, игнорируя ошибки доступа (файл занят работающим Chrome)."""
    try:
        shutil.copy2(src, dst)
    except (OSError, PermissionError):
        pass


shutil.copytree(
    original_profile_path,
    os.path.join(temp_user_data_dir, profile_directory),
    copy_function=_copy_ignore_locked,
)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument(f"--user-data-dir={temp_user_data_dir}")
options.add_argument(f"--profile-directory={profile_directory}")
# options.add_argument('--incognito')

# Добавление профиля
options.add_argument(f"user-data-dir={temp_user_data_dir}")
options.add_argument(f"profile-directory={profile_directory}")

driver = webdriver.Chrome(options=options)
driver.get("https://2ip.ru")
time.sleep(10)
print(f"Title: {driver.title}")
time.sleep(5)