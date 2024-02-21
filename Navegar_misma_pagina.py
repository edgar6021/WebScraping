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


pestana = chrome_driver
pestana.get('https://achirou.com')
time.sleep(1)

pestana = chrome_driver
pestana.get('https://microsft.com')
time.sleep(1)

pestana = chrome_driver
pestana.get('https://google.com')
time.sleep(1)

pestana = chrome_driver
pestana.get('https://gmail.com')
time.sleep(1)

pestana.back()
time.sleep(1)

pestana.back()
time.sleep(1)

pestana.forward()
time.sleep(1)

pestana.back()
time.sleep(1)

pestana.forward()
time.sleep(1)

pestana.quit()


