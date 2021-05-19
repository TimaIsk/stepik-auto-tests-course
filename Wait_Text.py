from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
#Ожидаем текст и жмакаем на кнопку
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element_by_xpath("//button[@id='book']").click()

#Поднимаем текст
    text = browser.find_element_by_xpath("//span[@id='simple_text']")
    browser.execute_script("return arguments[0].scrollIntoView({behavior: 'auto'});", text)

#Расчитываем формулу
    x = browser.find_element_by_xpath('//span[@id="input_value"]').text
    y = calc(x)
    x = browser.find_element_by_xpath('//input[@id="answer"]').send_keys(y)

#Кликаем решение
    browser.find_element_by_xpath("//button[@id='solve']").click()

#Ловим алерт
    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(2)
    browser.quit()
