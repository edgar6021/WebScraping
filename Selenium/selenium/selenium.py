import sys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_driver = webdriver.Chrome("C:\SeleniumDriver\chromedriver.exe")
chrome_driver.get('https://www.w3schools.com/html/html_forms.asp')

chrome_driver.find_element_by_id('fname').clear()

input_form = chrome_driver.find_element_by_id("fname")
input_form.send_keys('EDGAR')
