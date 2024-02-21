import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

# Path to your Chrome browser executable if needed
# chrome_options.add_argument("--binary-location=path/to/chrome.exe")

tablas = webdriver.Chrome(options=chrome_options)

tablas.get("https://www.w3schools.com/html/html_tables.asp")

# Use explicit wait to wait for the table to be present
wait = WebDriverWait(tablas, 10)
table = wait.until(EC.presence_of_element_located((By.ID, "customers")))

# Find all rows and columns in the table
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    for column in columns:
        print(column.text, end='  ')
    print()

tablas.quit()
