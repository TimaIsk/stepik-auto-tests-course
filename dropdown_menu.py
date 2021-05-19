from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

#Находим выпадающее меню и кликаем на него
browser.find_element_by_xpath('//select[@id="dropdown"]').click()
#Находим нужное значение
browser.find_element_by_xpath('//option[@value="1"]').click()
#Снова кликаем на меню для закрытия
browser.find_element_by_xpath('//select[@id="dropdown"]').click()
# Нажимаем на кнопку Submit.
button = browser.find_element_by_xpath("//button[@class='btn btn-default']").click()

# ловим алерт и забираем из него ответ
print(browser.switch_to.alert.text.split()[-1])

time.sleep(5)
browser.quit()

# не забываем оставить пустую строку в конце файла