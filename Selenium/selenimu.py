from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

os.environ['PATH'] += r"C:\SeleniumDriver"

driver = webdriver.Chrome()
driver.get("https://start.microsoftapp.net/start?pc_campaign=UHF_Banner_15mkts&adjust=y9xgnyl_5sblqid")

try:
    my_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'navbarCollapse')))
    my_element.click()
    
    # Here's where the change is
    my_element_second = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'myButton')))

    my_element_second.click()
finally:
    # Keep the browser open for 10 seconds
    time.sleep(10)
    # It's a good practice to quit the driver at the end of your script
    driver.quit()
