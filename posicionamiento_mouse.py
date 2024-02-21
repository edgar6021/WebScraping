from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-local-proxy")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
# If Chrome binary_location is in your system's PATH, you can omit this line.
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Use a context manager to manage the WebDriver instance
with webdriver.Chrome(options=chrome_options) as enlace:
    enlace.get("https://www.unnatec.do/unnatec-virtual/")
    
    # Use explicit waits with a different expected condition
    wait = WebDriverWait(enlace, 10)
    
    # Locate the anchor element by its class
    hipervinculo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "elementor-item-anchor")))

    # Move to the anchor element and click it
    with ActionChains(enlace) as posicionar:
        posicionar.move_to_element(hipervinculo).click().perform()
