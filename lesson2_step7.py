import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()

    try:
        browser.get(link)

        x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
        print(x)

        result = calc(x)

        in1 = browser.find_element(By.ID, "answer")
        in1.send_keys(result)

        checkBox1 = browser.find_element(By.ID, "robotCheckbox")
        checkBox1.click()

        op1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
        op1.click()

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    finally:
        time.sleep(15)
        browser.quit()
