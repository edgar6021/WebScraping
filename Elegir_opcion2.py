import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

class CustomSelectTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-local-proxy")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to your Chrome browser executable
        self.chrome_driver = webdriver.Chrome(options=chrome_options)
        self.chrome_driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')
        time.sleep(1)

    def test_custom_select(self):
        select_element = self.chrome_driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        options = select_element.find_elements_by_tag_name("option")

        for option in options:
            option.click()
            time.sleep(1)

        select = Select(select_element)
        select.select_by_value("7")

    def tearDown(self):
        self.chrome_driver.quit()

if __name__ == '__main__':
    unittest.main()
