import urllib.request
from bs4 import BeautifulSoup

pagina_web_url = input('Enter - ')
codigo = urllib.request.urlopen(pagina_web_url)
Beaut = BeautifulSoup(codigo, 'html.parser') # Added parser

P = Beaut.find_all('p')  # Changed 'P' to 'p'

texto = ''
for x in P:
    texto += x.get_text()  # Use get_text() instead of contents[0]
print(texto)
