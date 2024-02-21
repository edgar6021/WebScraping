import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-local-proxy")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")  # Add this line to ignore SSL errors
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to your Chrome browser executable
chrome_driver = webdriver.Chrome(options=chrome_options)


css = webdriver.Chrome(options=chrome_options)  # Create a new WebDriver instance
css.get("https://www.w3schools.com/html/default.asp")
time.sleep(2)
contenedor = css.find_element(By.CSS_SELECTOR, 'a.w3-blue')  # Use 'find_element' with the correct syntax
contenedor.click()
