import time
from selenium import webdriver
from selenium.webdriver.common.by import By

 # Заходим на указанную страницу
link = "http://suninjuly.github.io/find_xpath_form" 
    

try:
    # Подключаемся к браузеру Chrome
    browser = webdriver.Chrome()
    browser.get(link)

        # Заполняем форму регистрации
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()
    time.sleep(15)
    
  
finally:
    # Закрываем браузер
    browser.quit()