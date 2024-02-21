import urllib.request
from bs4 import BeautifulSoup

pagina_web_url= input('Enter - ')
codigo = urllib.request.urlopen(pagina_web_url)
Beaut = BeautifulSoup(codigo)

elemento = Beaut('a')
for x in elemento:
    print(x.get('href'))