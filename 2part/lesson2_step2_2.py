from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

if __name__ == '__main__':

    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    browser.find_element(By.CSS_SELECTOR, "[value='" + str(int(num1) + int(num2)) + "']").click()

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
