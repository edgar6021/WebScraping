from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

scroll = webdriver.Chrome(options=chrome_options)


scroll.get("https://www.unnatec.do/unnatec-virtual/")
time.sleep(2)
scroll.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
scroll.quit()