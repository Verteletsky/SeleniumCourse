from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # accept = browser.switch_to.alert
    # accept.accept()
    #
    # x = browser.find_element(By.ID, "input_value").text
    #
    # browser.find_element(By.ID, "answer").send_keys(calc(x))
    #
    # browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, "file.txt")
    #
    # browser.find_element(By.NAME, "firstname").send_keys("Roman")
    # browser.find_element(By.NAME, "lastname").send_keys("Verteletsky")
    # browser.find_element(By.NAME, "email").send_keys("verteletsky@bitrix24.ru")
    # browser.find_element(By.ID, "file").send_keys(file_path)
