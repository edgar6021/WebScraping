from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

cookie = webdriver.Chrome(options=chrome_options)
cookie.get("https://www.infojobs.net/ofertas-trabajo/hacking-etico")
all_cokie = cookie.get_cookies()
print(all_cokie)


