from selenium.webdriver.common.by import By
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
button.click()