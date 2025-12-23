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
    # 1. Открыть страницу
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # 2. Нажать кнопку
    browser.find_element(By.TAG_NAME, "button").click()

    # 3. Принять confirm
    alert = browser.switch_to.alert
    alert.accept()

    # 4. Решить капчу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    # 5. Нажать Submit (самый надёжный локатор)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(5)

finally:
    browser.quit()




