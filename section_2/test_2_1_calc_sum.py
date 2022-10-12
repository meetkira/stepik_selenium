from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


def calc(x, y):
  return str(int(x)+int(y))


link = "http://suninjuly.github.io/selects2.html"
#link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")
    result = calc(x.text, y.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    res = select.select_by_visible_text(result)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
