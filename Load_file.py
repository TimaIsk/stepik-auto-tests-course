from selenium import webdriver
import time, os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element_by_xpath('//input[@placeholder="Enter first name"]').send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Enter last name"]').send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Enter email"]').send_keys("asdv@asd.asd")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_xpath("//input[@id='file']").send_keys(file_path)
    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(2)
    browser.quit()