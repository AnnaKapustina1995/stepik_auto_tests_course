from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

# функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# запуск браузера
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. Открываем страницу
    browser.get("https://suninjuly.github.io/math.html")

    # 2. Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 3. Вычисляем значение функции
    y = calc(x)

    # 4. Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 5. Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # 6. Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # 7. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # пауза, чтобы увидеть результат
    time.sleep(5)

finally:
    browser.quit()
