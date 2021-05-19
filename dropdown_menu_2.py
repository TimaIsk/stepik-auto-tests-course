from selenium.webdriver.support.ui import Select #Инициализация пакета SELECT
from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

select = Select(browser.find_element_by_xpath('//select[@id="dropdown"]'))
select.select_by_value("1") # ищем элемент с текстом "Python"

#Вариант 1: select.select_by_visible_text("text")
    #Первый способ ищет элемент по видимому тексту, например,
    #select.select_by_visible_text("Python") найдёт "Python" для нашего примера.

#Вариант2: select.select_by_index(index)
    #Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля.
    #Для того чтобы найти элемент с текстом "Python", нужно использовать select.select_by_index(1),
    #так как опция с индексом 0 в данном примере имеет значение по умолчанию равное "--".

time.sleep(5)
browser.quit()

# не забываем оставить пустую строку в конце файла