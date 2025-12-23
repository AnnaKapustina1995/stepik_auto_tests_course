from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Можно менять ссылку между selects1 и selects2
    browser.get("https://suninjuly.github.io/selects1.html")
    # browser.get("https://suninjuly.github.io/selects2.html")

    # 1) Считать числа
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # 2) Посчитать сумму
    total = str(int(num1) + int(num2))

    # 3) Найти выпадающий список
    select = Select(browser.find_element(By.TAG_NAME, "select"))

    # 4) Выбрать значение, равное сумме
    select.select_by_value(total)

    # 5) Нажать Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(5)

finally:
    browser.quit()
