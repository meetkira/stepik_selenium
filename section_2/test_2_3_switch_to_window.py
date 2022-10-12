import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button").click()

    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, "input_value")
    result = calc(x.text)
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(result)

    browser.find_element(By.TAG_NAME, "button").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
