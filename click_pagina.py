
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

click = webdriver.ChromeOptions()
click.add_argument("--ignore-local-proxy")
click.add_argument("--ignore-certificate-errors")
click.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver = webdriver.Chrome(options=click)
chrome_driver.get('https://www.jigsawplanet.com/?rc=signin')

click_en_campo = 'input[name="usernameemail"]'
accion = WebDriverWait(chrome_driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, click_en_campo))
)

accion.click()
time.sleep(30)
