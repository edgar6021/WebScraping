import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

direccion = input('Enter url: ')
codigo = urllib.request.urlopen(direccion)
bea = BeautifulSoup(codigo, 'html.parser') # Added parser
p = bea('p')

texto = '' 
for x in p:
    if (len(x.attrs)) == 0:
        a= x.contents[0]
        texto = str(texto) + str(a)

almacenar_contar = dict()
texto = texto.replace(',','').replace('.','').replace(':','').replace('?','').replace('¿','').replace('!','').replace('¡','').replace('(','').replace(')','').replace('“','').replace('”','')
letras = texto.lower().split()
for x in letras:
    almacenar_contar[x] = almacenar_contar.get(x,0) + 1

df = pd.DataFrame(list(almacenar_contar.items()), columns=['palabra', 'contador'])
df_sorted = df.sort_values('contador', ascending=False)

print(df_sorted)
