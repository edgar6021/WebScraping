import requests
from bs4 import BeautifulSoup
import csv

url = 'https://hoopshype.com/salaries/players/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'hh-salaries-ranking-table'})
player_data = []
for row in table.find_all('tr')[1:]:
    player_name = row.find('td', {'class': 'name'}).text.strip()
    player_salary = row.find('td', {'class': 'hh-salaries-sorted'}).text.strip()
    player_data.append((player_name, player_salary))
for i in range(len(player_data)):
    salary_list = player_data[i][1].replace('$', '').replace(',', '').split('-')
    
    if len(salary_list) == 1:
        average_salary = float(salary_list[0])
    else:
        average_salary = (float(salary_list[0]) + float(salary_list[1])) / 2
    player_data[i] = (player_data[i][0], player_data[i][1], average_salary)
with open('jugadores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Jugador', 'Salario', 'Salario promedio'])
    for player in player_data:
        writer.writerow([player[0], player[1], player[2]])