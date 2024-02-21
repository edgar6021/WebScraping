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
chrome_driver.get('https://www.w3schools.com/html/html_forms.asp')

input_form = WebDriverWait(chrome_driver, 10).until(
    EC.visibility_of_element_located((By.ID, "lname"))
)
input_form.clear()
input_form.send_keys('gancho')

input_form2 = WebDriverWait(chrome_driver, 10).until(
    EC.visibility_of_element_located((By.ID, "fname"))
)
input_form2.clear()
input_form2.send_keys('Puero')

# Esperar un momento antes de cerrar el navegador
time.sleep(2)

# Cerrar el navegador
chrome_driver.quit()
