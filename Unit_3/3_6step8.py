import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")