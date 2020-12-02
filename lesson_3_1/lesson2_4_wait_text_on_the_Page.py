from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(text_to_be_present_in_element((By.ID, "price"), "100"))

    bookButton = browser.find_element_by_id("book")
    bookButton.click()

    buttonSubmit = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", buttonSubmit)
    elementValue = browser.find_element_by_id("input_value")
    getValue = int(elementValue.text)  # numI = int(browser.find_element_by_id("input_value").text)
    final_result = calc(getValue)

    textField = browser.find_element_by_id("answer")
    textField.send_keys(final_result)
    buttonSubmit.click()

finally:
    time.sleep(11)
    browser.quit()

