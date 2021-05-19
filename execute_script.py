from selenium import webdriver
import math, time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
# Решение формулы
    x = browser.find_element_by_xpath('//span[@id="input_value"]').text
    y = calc(x)
    x = browser.find_element_by_xpath('//input[@id="answer"]').send_keys(y)

# Поднять кнопку на видное место
    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    browser.execute_script("return arguments[0].scrollIntoView({behavior: 'auto'});", button)

# Тык и тык на чек бокс и радио баттон
    option1 = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    option2 = browser.find_element_by_xpath("//input[@id='robotsRule']").click()

    button.click()

    # ловим алерт и забираем из него ответ
    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(1)
    browser.quit()

# не забываем оставить пустую строку в конце файла