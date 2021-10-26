from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector('#treasure')
    treasure_value = (x_element.get_attribute("valuex"))
    x = treasure_value
    y = calc(x)
    
	# Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys (y)
    option1 = browser.find_element_by_css_selector('#robotCheckbox')
    option1.click()
    option1 = browser.find_element_by_css_selector('#robotsRule')
    option1.click()

    # ждем загрузки страницы
    time.sleep(3)

	# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
