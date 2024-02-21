import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-local-proxy")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to your Chrome browser executable
chrome_driver = webdriver.Chrome(options=chrome_options)



navegar = chrome_driver
navegar.get('https://achirou.com')
time.sleep(2)
navegar.execute_script("window.open('');")
time.sleep(2)
navegar.switch_to.window(navegar.window_handles[1])

navegar.get('https://google.com')
time.sleep(2)
navegar.execute_script("window.open('');")
time.sleep(2)
navegar.switch_to.window(navegar.window_handles[2])

navegar.get('https://educa.mastech.academy')
time.sleep(2)
navegar.execute_script("window.open('');")
time.sleep(2)
navegar.switch_to.window(navegar.window_handles[0])