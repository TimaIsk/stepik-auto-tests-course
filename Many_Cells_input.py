from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Мой ответ") #Заполняет все найденные ячейки текстом

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ловим алерт и забираем из него ответ
    print(browser.switch_to.alert.text.split()[-1])

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла