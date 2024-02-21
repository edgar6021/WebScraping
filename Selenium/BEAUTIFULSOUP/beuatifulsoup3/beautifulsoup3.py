import urllib.request
from bs4 import BeautifulSoup

pagina_web_url = input('Enter - ')
codigo = urllib.request.urlopen(pagina_web_url)
beat = BeautifulSoup(codigo)

elemento = beat('a')
for x in elemento:
    print('Elemento "a" completa:', x)
    print('Direccion:', x.get('href'))
    print('Contenido:', x.contents)
    print('Atributo:', x.attrs)
    print('\n')