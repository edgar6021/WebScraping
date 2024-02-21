from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

scraping = webdriver.Chrome(options=chrome_options)

scraping.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
time.sleep(2)
boton=scraping.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
boton.click()
time.sleep(2)
boton=scraping.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[3]")
boton.click()
time.sleep(2)