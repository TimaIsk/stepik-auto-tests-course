from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    alert = browser.switch_to.alert #Переключение на АЛЕРТ окно
    alert.accept()

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]').text
    y = calc(x_element)
    x_element = browser.find_element_by_xpath('//input[@id="answer"]').send_keys(y)
    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(2)
    browser.quit()

#Пустая строка