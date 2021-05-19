from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

#ищем значение Х преобразовываем в text и подставляем в формулу + записываем это значение в переменную У
x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
x = x_element.text
y = calc(x)

#ищем поле и вводим значение
x_element = browser.find_element_by_xpath('//input[@id="answer"]')
x_element.send_keys(y)

# Отмечаем checkbox "I'm the robot"
option1 = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()

#Выбираем radiobutton "Robots rule!"
option2 = browser.find_element_by_xpath("//input[@id='robotsRule']").click()

# Нажимаем на кнопку Submit.
button = browser.find_element_by_xpath("//button[@class='btn btn-default']").click()

# ловим алерт и забираем из него ответ
print(browser.switch_to.alert.text.split()[-1])

time.sleep(2)
browser.quit()

# не забываем оставить пустую строку в конце файла