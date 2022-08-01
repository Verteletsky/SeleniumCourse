from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()

try:
    browser.get(link)

    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(text)

    find_link = browser.find_element(By.LINK_TEXT, text)
    find_link.click()

    in1 = browser.find_element(By.NAME, "first_name")
    in1.send_keys("Roman")

    in2 = browser.find_element(By.NAME, "last_name")
    in2.send_keys("Verteletsky")

    in3 = browser.find_element(By.CLASS_NAME, "city")
    in3.send_keys("Volgograd")

    in4 = browser.find_element(By.ID, "country")
    in4.send_keys("Russia")

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
