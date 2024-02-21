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

# Extraer los nombres de los jugadores y sus salarios
player_data = []
for row in table.find_all('tr')[1:]:
    player_name = row.find('td', {'class': 'name'}).text.strip()
    player_salaries = []
    for salary_td in row.find_all('td')[2:]:
        salary = salary_td['data-value']
        player_salaries.append(float(salary))
    player_data.append((player_name, player_salaries))

# Calcular el salario promedio de cada jugador
average_salaries = []
for player_name, salaries in player_data:
    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)
    average_salaries.append((player_name, average_salary))

# Guardar los datos en un archivo CSV
with open('Salarios y promedios de jugadores por temporada.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Salario Promedio', 'Salarios', '2023/24',	'2024/25',	'2025/26','2026/27', '2027/28'])
    for i, (player_name, salaries) in enumerate(player_data):
        writer.writerow([player_name, average_salaries[i][1]] + [f'${salary:,.2f}' for salary in salaries])
