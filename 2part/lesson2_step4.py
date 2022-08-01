from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    in1 = browser.find_element(By.ID, "input_value")

    result = calc(in1.text)

    button = browser.find_element(By.TAG_NAME, "button")

    enter = browser.find_element(By.ID, "answer")
    enter.send_keys(result)

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

    button.click()
