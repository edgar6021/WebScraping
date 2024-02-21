from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

try:
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")

    # Wait for the switch element to be clickable before interacting with it
    switch = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/label[3]/div")))
    
    # Click the switch to toggle its state
    switch.click()

    # Wait for the switch state to be updated (optional)
    # time.sleep(2)

    # Click the switch again to toggle its state back
    switch.click()

    # Wait for the switch state to be updated (optional)
    # time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

