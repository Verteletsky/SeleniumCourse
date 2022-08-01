from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    btn = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    val1 = browser.find_element(By.ID, "input_value").text

    browser.find_element(By.ID, "answer").send_keys(calc(val1))

    browser.find_element(By.ID, "solve").click()

    # message = browser.find_element(By.ID, "verify_message")

    # assert "successful" in message.text
