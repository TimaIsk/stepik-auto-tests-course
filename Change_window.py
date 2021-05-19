from selenium import webdriver
import time, math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = ("http://suninjuly.github.io/redirect_accept.html")
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window) #Переключение на второе окно, счет идёт с 0

    x_element = browser.find_element_by_xpath('//span[@id="input_value"]').text
    y = calc(x_element)
    x_element = browser.find_element_by_xpath('//input[@id="answer"]').send_keys(y)
    button2 = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(2)
    browser.quit()
