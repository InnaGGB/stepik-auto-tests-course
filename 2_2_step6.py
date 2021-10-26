from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector('#input_value.nowrap')
    x = x_element.text
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
	
	# Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys (y)
    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()
    option1 = browser.find_element_by_css_selector('#robotsRule')
    option1.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
	
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()