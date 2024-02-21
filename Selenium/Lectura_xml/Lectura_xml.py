import urllib.request
import xml.etree.ElementTree as xml

pag = 'https://www.w3schools.com/xml/simple.xml'

inf = urllib.request.urlopen(pag).read()
o = xml.fromstring(inf.decode()) 

t= o.findall('food')
print('cant of registre', len(t))

for r in t:
    print('\r')
    print('Name:', r.find('name').text)
    print('Price:', r.find('price').text)
    print('Description', r.find('description').text)
    print('Calories', r.find('calories').text)