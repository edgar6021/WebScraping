import sys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-local-proxy")
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to your Chrome browser executable
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get('https://www.w3schools.com/html/html_forms.asp')

input_form = chrome_driver.find_element("id", "fname")
input_form.clear()
input_form.send_keys('EDGAR')
