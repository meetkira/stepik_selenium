import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 10 секунд, пока кнопка не станет кликабельной
    element = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value")
    result = calc(x.text)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(result)

    browser.find_element(By.ID, "solve").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
