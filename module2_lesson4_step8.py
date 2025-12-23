from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # 1) Ждём, пока цена станет $100 (таймаут не меньше 12 сек)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2) Нажимаем Book
    browser.find_element(By.ID, "book").click()

    # 3) Решаем капчу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    # 4) Submit
    browser.find_element(By.ID, "solve").click()

    time.sleep(5)

finally:
    browser.quit()





