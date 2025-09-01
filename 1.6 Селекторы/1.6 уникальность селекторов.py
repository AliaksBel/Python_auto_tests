import time
from selenium import webdriver
from selenium.webdriver.common.by import By

 # Заходим на указанную страницу
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Уникальные селекторы для полей ввода
    first_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name_input.send_keys("Иван")

    second_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    second_name_input.send_keys("Иванов")

    email_input = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email_input.send_keys("example@mail.ru")

    phone_input = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    phone_input.send_keys("+79991234567")

    address_input = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    address_input.send_keys("Москва, ул. Пушкина, д. 1")
    time.sleep(10)

    # Поиск кнопки Submit и клик по ней
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Пауза для проверки результата
    time.sleep(1)

finally:
    # Закрываем браузер
    browser.quit()