from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
	# Нажимаем на кнопку
    button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button.click()
	
	# Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
    
	
    x_element = browser.find_element_by_css_selector('#input_value.nowrap')
    x = x_element.text
    y = calc(x)
	
	# Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys (y)
	
	# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
	
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
	