from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    numI = int(browser.find_element_by_id("input_value").text)
    num2 = calc(numI)

    textField = browser.find_element_by_class_name("form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", textField)
    textField.send_keys(num2)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radioButton = browser.find_element_by_id("robotsRule")
    radioButton.click()

    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()