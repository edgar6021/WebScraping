from selenium.webdriver.common.by import By
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

cargar=webdriver.Chrome(options=chrome_options)

cargar.get("https://mdbootstrap.com/plugins/jquery/file-upload/")
time.sleep(2)
cargar.find_element_by_id("customFile").send_keys("C:\\Users\\Usuario\\Desktop\\webScraping\\Screem\\youtube.png")