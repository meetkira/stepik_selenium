import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("first_name")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("last_name")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("email")

    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'myfile.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
