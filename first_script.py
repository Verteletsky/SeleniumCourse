import time

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        in1 = browser.find_element(By.TAG_NAME, "input")
        in1.send_keys("Ivan")

        in2 = browser.find_element(By.NAME, "last_name")
        in2.send_keys("Petrov")

        in3 = browser.find_element(By.CLASS_NAME, "firstname")
        in3.send_keys("Smolensk")

        in4 = browser.find_element(By.ID, "country")
        in4.send_keys("Russia")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()
    # driver = webdriver.Chrome()
    #
    # time.sleep(5)
    #
    # driver.get("https://stepik.org/lesson/25969/step/12")
    # time.sleep(5)
    #
    # textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
    #
    # textarea.send_keys("get()")
    # time.sleep(5)
    #
    # submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
    #
    # submit_button.click()
    # time.sleep(5)
    #
    # driver.quit()
