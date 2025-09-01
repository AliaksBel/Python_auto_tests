'''from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


x_element = WebDriverWait(browser, 120).until(
    EC.text_to_be_present_in_element((By.ID, "price"))
)
button = browser.find_element(By.ID, "book")
button.click()'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Определяем функцию для расчёта математического выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждём, пока цена домика уменьшится до $100 (максимальное ожидание 12 секунд)
    wait = WebDriverWait(browser, 12)
    price_element = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Находим значение x из скрытого поля
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим результат в текстовое поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # Нажимаем кнопку "Solve"
    solve_button = browser.find_element(By.ID, "solve")
    solve_button.click()

finally:
    # Ждём пару секунд, чтобы увидеть результат
    time.sleep(5)
    # Закрываем браузер
    browser.quit()