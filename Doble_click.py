from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-local-proxy")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
# If Chrome binary_location is in your system's PATH, you can omit this line.
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

double_click = webdriver.Chrome(options=chrome_options)
double_click.get("https://www.unnatec.do/unnatec-virtual/")
time.sleep(2)

# Use explicit wait with visibility_of_element_located
wait = WebDriverWait(double_click, 10)
accion = wait.until(EC.visibility_of_element_located((By.XPATH, "//svg[@data-test='your-target-element']")))

real = ActionChains(double_click)
real.double_click(accion).perform()
real.context_click(accion).perform()
