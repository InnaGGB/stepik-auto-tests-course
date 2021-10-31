from selenium import webdriver
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
	# Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('input[placeholder="Enter first name"]')
    input1.send_keys("Inna")
    input2 = browser.find_element_by_css_selector('input[placeholder="Enter last name"]')
    input2.send_keys("GGB")
    input3 = browser.find_element_by_css_selector('input[placeholder="Enter email"]')
    input3.send_keys("qwerty@mail.com")
	
	# получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
	# добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_css_selector('#file')    
    element.send_keys(file_path)
	
	# Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
	
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()