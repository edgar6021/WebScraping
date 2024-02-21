import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_argument("--ignore-local-proxy")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_driver = webdriver.Chrome(options=chrome_options)

try:
    chrome_driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')

    # Wait for the custom select element to be visible
    custom_select = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "custom-select"))
    )

    # Find the select element within the custom select
    seleccionar = custom_select.find_element(By.TAG_NAME, "select")

    # Get all the options within the select element
    opciones = seleccionar.find_elements(By.TAG_NAME, "option")

    for s in opciones:
        # Scroll the custom select element into view before clicking
        chrome_driver.execute_script("arguments[0].scrollIntoView(true);", custom_select)
        # Click on each option
        s.click()
        time.sleep(1)

    # Select an option by its value
    mostrar = Select(seleccionar)
    mostrar.select_by_value("7")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    chrome_driver.quit()
