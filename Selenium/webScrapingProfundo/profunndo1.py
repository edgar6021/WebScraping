import urllib.request
from bs4 import BeautifulSoup

pagina_web_url = input('Enter - ')
codigo = urllib.request.urlopen(pagina_web_url)
Beaut = BeautifulSoup(codigo)

elemento = Beaut('a')
print('Enlaces en la pagina Principal; \r\n')
for x in elemento:
    print (x.contents[0], x.get('href'))
    
    print('\r\n Enlaces en la paginas secundarias: \r\n')
    
for x in elemento:
    nueva_url = x.get('href', None)
    print('* Accediendo a los enlances dentro de la pagina: ' + nueva_url)
    try:
        if nueva_url[0:4]=='http':codigo2 = urllib.request.urlopen(nueva_url) 
        else: codigo2 = urllib.request.urlopen(pagina_web_url + nueva_url)
        Beaut2 = BeautifulSoup(codigo2)
        nuevo_elemento = Beaut2('a')
        if len(nuevo_elemento)>0:
            print(len(nuevo_elemento), 'Enlaces:')
            for y in nuevo_elemento:
                print(y.get('href'))
        else: print('No tienes mas enlaces')
    except: print('No se puede acceder a la pagina')
