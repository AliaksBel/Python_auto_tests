import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Определение функции расчета
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем браузер и загружаем нужную страницу
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    time.sleep(1)

    # Находим элемент, содержащий число X
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # Рассчитываем значение Y с помощью функции calc
    y = calc(x)

    # Находим текстовое поле и вводим туда посчитанное значение Y
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)
    time.sleep(1)

    # Ставим отметку на чекбокс "I'm the robot"
    checkbox_robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_robot.click()
    time.sleep(1)

    # Выбираем радиобаттон "Robots rule!"
    radio_robots_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_robots_rule.click()
    time.sleep(1)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    time.sleep(1)

finally:
    # Оставляем пауза на 10 сек., чтобы успеть увидеть результат
    time.sleep(10)
    # Закрываем браузер
    browser.quit()