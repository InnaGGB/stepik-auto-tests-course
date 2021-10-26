from selenium import webdriver
import time
import unittest


class TestReg(unittest.TestCase):

    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")
        browser.find_element_by_css_selector(".first_block .third").send_keys("qwerty@test.ru")

        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")
        browser.find_element_by_css_selector(".first_block .third").send_keys("qwerty@test.ru")

        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


if __name__ == "__main__":
    unittest.main()