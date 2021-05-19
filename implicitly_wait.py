from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

try:
    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    message = browser.find_element_by_xpath("//div[@id='verify_message']")

    assert "Verification was successful!" in message.text

finally:
    browser.quit()