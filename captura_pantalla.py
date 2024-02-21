from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

captura = webdriver.Chrome(options=chrome_options)

captura.get("https://www.youtube.com/watch?v=Va8ZUBbmg48&t=616s")
captura.get_screenshot_as_file("C:\\Users\\Usuario\Desktop\\webScraping\\Screem\\youtube.png")