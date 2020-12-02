from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    digit = int(browser.find_element_by_id("input_value").text)
    result = calc(digit)

    answear = browser.find_element_by_id("answer")
    answear.send_keys(result)

    submitButton = browser.find_element_by_class_name("btn-primary")
    submitButton.click()

finally:
    time.sleep(11)
    browser.quit()