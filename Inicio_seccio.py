import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-local-proxy")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Path to your Chrome browser executable
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get('https://login.one.com/mail')

correo = WebDriverWait(chrome_driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "displayUsername"))
    
)

correo.send_keys("juan@gmail.com")

time.sleep(2)

correo = WebDriverWait(chrome_driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "password"))
    
)

correo.send_keys("123456789")

time.sleep(2)

correo.send_keys(Keys.ENTER)


time.sleep(10)

chrome_driver.quit()