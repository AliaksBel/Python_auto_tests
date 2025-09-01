import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # Подключаемся к браузеру Chrome
    browser = webdriver.Chrome()

    # Заходим на указанную страницу
    link = "http://suninjuly.github.io/find_link_text"
    browser.get(link)

    # Вычисляем шифр, указанный в задаче
    secret_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    # Находим ссылку с нужным текстом и кликаем по ней
    element = browser.find_element(By.PARTIAL_LINK_TEXT, secret_text)
    element.click()
    #time.sleep(7)'''

    # Заполняем форму регистрации
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(15)
    
    # Ждём появления результата и выводим его на экран
    alert = browser.switch_to.alert
    result = alert.text.split()[-1]
    print(result)
    alert.accept()

finally:
    # Закрываем браузер
    browser.quit()