from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x,z):
  return str(int(x)+int(z)) 


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector('#num1')
    x = x_element.text
    z_element = browser.find_element_by_css_selector('#num2')
    z = z_element.text
    y = calc(x,z)
    
	# Код, который выбирает в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)  
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