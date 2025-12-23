from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get("https://suninjuly.github.io/execute_script.html")

    # 1) Считать x
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # 2) Ввести ответ
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # 3) Чекбокс и радиокнопка
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    radio = browser.find_element(By.ID, "robotsRule")

    # 4) Проскроллить, чтобы элементы точно были видимы (футер мешает)
    browser.execute_script("arguments[0].scrollIntoView(true);", checkbox)

    checkbox.click()
    radio.click()

    # 5) Скроллим к кнопке и жмём Submit
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(5)

finally:
    browser.quit()

