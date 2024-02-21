import requests
from bs4 import BeautifulSoup
import csv

# Hacer una solicitud HTTP a la página web
url = 'https://hoopshype.com/salaries/players/'
response = requests.get(url)

# Analizar el HTML de la página usando BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la tabla que contiene los datos de los jugadores y sus salarios
table = soup.find('table', {'class': 'hh-salaries-ranking-table'})

# Extraer los nombres de los jugadores, sus salarios por temporada y las fechas de cada temporada
player_data = []
for row in table.find_all('tr')[1:]:
    player_name = row.find('td', {'class': 'name'}).text.strip()
    player_salary = row.find_all('td', {'class': 'hh-salaries-sorted'})
    salary_list = [salary.text.strip() for salary in player_salary]
    salary_dates = row.find_all('td', {'class': 'hh-salaries-sorted'})
    dates_list = []
    for date in salary_dates:
        if date.find('span') is not None:
            dates_list.append(date.find('span').get('data-original-title'))
        elif date.get('data-original-title') is not None:
            dates_list.append(date.get('data-original-title'))
        else:
            dates_list.append('')
    player_data.append((player_name, salary_list, dates_list))

# Escribir los datos en un archivo CSV
with open('tabla_salarios.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    header = ['PLAYER']
    for date in player_data[0][2]:
        header.append(date)
    writer.writerow(header)
    for i in range(len(player_data)):
        row = [player_data[i][0]]
        for j in range(len(player_data[i][1])):
            row.append(player_data[i][1][j])
        writer.writerow(row)
