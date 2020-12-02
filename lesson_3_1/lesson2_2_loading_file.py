from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'Meet - ofm-caea-ozk - Google Chrome 2020-09-04 151..png')           # добавляем к этому пути имя файла

try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element_by_css_selector('[name="firstname"]')
    firstName.send_keys("Viktoriia")

    lastName = browser.find_element_by_css_selector('[name="lastname"]')
    lastName.send_keys("Pozdniakova")

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys("angelinaevans22@gmail.com")

    chooseFileButton = browser.find_element_by_id("file")
    chooseFileButton.send_keys(file_path)


    buttonSubmit = browser.find_element_by_css_selector('[type = "submit"]')
    buttonSubmit.click()

finally:
    time.sleep(11)
    browser.quit()



