import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Opciones = webdriver.ChromeOptions()
Opciones.add_argument("--ignore-local-proxy")
Opciones.add_argument("--ignore-certificate-errors")
Opciones.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver = webdriver.Chrome(options=Opciones)
chrome_driver.get('https://eportal.miteco.gob.es/BoleHWeb/')

option = 'select[name="year"] option[value="12"]'
accion = WebDriverWait(chrome_driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, option))
)

accion.click()

option3 = 'select[name="month"] option[value="5"]'
accion3 = WebDriverWait(chrome_driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, option3))
)

accion3.click()

time.sleep(30)
chrome_driver.quit()
