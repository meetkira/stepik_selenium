import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def test_can_register(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
            input1.send_keys("Ivan")
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
            input1.send_keys("Ivan")
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
            input1.send_keys("Ivan")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            right_text = "Congratulations! You have successfully registered!"
            self.assertEqual(right_text, welcome_text, f"Wrong text! Expected {right_text}, got {welcome_text} instead")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()



    def test_cant_register(self):
        try:
            error_link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(error_link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
            input1.send_keys("Ivan")
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
            input1.send_keys("Ivan")
            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
            input1.send_keys("Ivan")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            right_text = "Congratulations! You have successfully registered!"
            self.assertEqual(right_text, welcome_text, f"Wrong text! Expected {right_text}, got {welcome_text} instead")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
