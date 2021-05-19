from selenium.webdriver.support.ui import Select #Инициализация пакета SELECT
from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
      x = browser.find_element_by_xpath('//span[@id="num1"]').text
      y = browser.find_element_by_xpath('//span[@id="num2"]').text
      res = str(int(x) + int(y))
      select = Select(browser.find_element_by_xpath('//select[@id="dropdown"]'))
      select.select_by_value(res) #Выбираем значение суммы чисел
      button = browser.find_element_by_xpath('//button[text()="Submit"]').click()

      #Получает ответ от окошка
      print(browser.switch_to.alert.text.split()[-1])

finally:
      time.sleep(3)
      browser.quit()

# не забываем оставить пустую строку в конце файла