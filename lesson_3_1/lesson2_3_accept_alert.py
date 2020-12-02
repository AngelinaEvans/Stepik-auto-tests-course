from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    clickButton = browser.find_element_by_class_name("btn-primary")
    clickButton.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    digit = int(browser.find_element_by_id("input_value").text)
    answear = calc(digit)

    textField = browser.find_element_by_id("answer")
    textField.send_keys(answear)

    submitButton = browser.find_element_by_class_name("btn-primary")
    submitButton.click()

finally:
    time.sleep(10)
    browser.quit()




