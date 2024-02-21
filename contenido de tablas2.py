from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

tablas = webdriver.Chrome(options=chrome_options)

tablas.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(2)

fila = len(tablas.find_elements("xpath", "//*[@id='customers']/tbody/tr"))
colum = len(tablas.find_elements("xpath", "//*[@id='customers']/tbody/tr[1]/th"))

for f in range(2, fila + 1):
    for c in range(1, colum + 1):
        imprimir = tablas.find_element("xpath", f"//*[@id='customers']/tbody/tr[{f}]/td[{c}]").text
        print(imprimir, end='  ')
    print()

tablas.quit()
