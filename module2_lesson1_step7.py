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
    # 1) Открыть страницу
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # 2-3) Найти сундук и взять x из атрибута valuex
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")

    # 4) Посчитать функцию
    y = calc(x)

    # 5) Ввести ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # 6) Отметить чекбокс
    browser.find_element(By.ID, "robotCheckbox").click()

    # 7) Выбрать радиобаттон
    browser.find_element(By.ID, "robotsRule").click()

    # 8) Нажать Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(5)

finally:
    browser.quit()
