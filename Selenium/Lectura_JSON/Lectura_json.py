import json

file_path = r"C:\Users\Usuario\Desktop\webScraping\Selenium\Lectura_JSON\clase.json"

with open(file_path, "r") as abrir:
    leer = json.load(abrir)

print('Number of persons:', len(leer))

for g in leer:
    print('\n')
    print('Name:', g['nombre'])
    print('Pais:', g['pais'])
    print('Telefono:', g['telefono'])
