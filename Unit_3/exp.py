import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_searching_ufo_messages(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element_by_tag_name('textarea').send_keys(str(math.log(int(time.time()))))
    #time.sleep(5)
    browser.find_element_by_css_selector("button.submit-submission").click()
    #time.sleep(10)
    message = browser.find_element_by_class_name('smart-hints__hint')
    m1 = message.text
    assert m1 == "Correct!", \
    f"got '{m1}' instead of 'Correct!'"
    #pytest -s -v c:\Users\sh-no\selenium_course\exp.py