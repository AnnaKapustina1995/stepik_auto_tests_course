from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1) Открыть страницу
    browser.get("http://suninjuly.github.io/file_input.html")

    # 2) Заполнить поля
    browser.find_element(By.NAME, "firstname").send_keys("Anna")
    browser.find_element(By.NAME, "lastname").send_keys("Ivanova")
    browser.find_element(By.NAME, "email").send_keys("test@test.com")

    # 3) Подготовить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test_file.txt")

    # создаём файл, если его нет
    with open(file_path, "w") as file:
        file.write("")

    # 4) Загрузить файл
    browser.find_element(By.ID, "file").send_keys(file_path)

    # 5) Нажать Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(5)

finally:
    browser.quit()


