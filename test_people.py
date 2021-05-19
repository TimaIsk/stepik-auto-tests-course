from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


def calc(a, b):
    return str(int(a) + int(b))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_xpath("//span[@id='num1']")
    a = number1.text
    number2 = browser.find_element_by_xpath("//span[@id='num2']")
    b = number2.text
    c = calc(a, b)

    choose = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))
    choose.select_by_visible_text(c)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()