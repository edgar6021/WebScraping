import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor

# Hacer una solicitud HTTP a la página web
url = 'https://hoopshype.com/salaries/players/'
response = requests.get(url)

# Analizar el HTML de la página usando BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la tabla que contiene los datos de los jugadores y sus salarios
table = soup.find('table', {'class': 'hh-salaries-ranking-table'})

# Extraer los nombres de los jugadores y las URLs de sus páginas individuales
player_data = []
for row in table.find_all('tr')[1:]:
    player_name = row.find('td', {'class': 'name'}).text.strip()
    player_url = row.find('td', {'class': 'name'}).find('a')['href']
    player_data.append((player_name, player_url))

# Función para extraer los salarios de todas las temporadas de un jugador
def get_player_salaries(player_url):
    time.sleep(1)  # Agregar un tiempo de espera antes de cada solicitud
    player_response = requests.get(player_url)
    player_soup = BeautifulSoup(player_response.content, 'html.parser')
    salary_table = player_soup.find('table', {'class': 'hh-salaries-ranking-table'})
    
    salaries = []
    if salary_table:
        for row in salary_table.find_all('tr')[1:]:
            season = row.find_all('td')[0].text.strip()
            salary = row.find_all('td')[1].text.strip()
            salaries.append((season, salary))
    return salaries

# Función auxiliar para ejecutar la función get_player_salaries con ThreadPoolExecutor
def process_player(player):
    player_name, player_url = player
    player_salaries = get_player_salaries(player_url)
    return (player_name, player_salaries)

# Extraer los salarios de todas las temporadas para cada jugador utilizando ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    player_data = list(executor.map(process_player, player_data))

# Calcular el salario promedio de cada temporada
season_totals = {}
for _, player_salaries in player_data:
    for season, salary in player_salaries:
        salary_value = float(salary.replace('$', '').replace(',', ''))
        if season not in season_totals:
            season_totals[season] = {'total_salary': salary_value, 'count': 1}
        else:
            season_totals[season]['total_salary'] += salary_value
            season_totals[season]['count'] += 1

average_salaries = {season: info['total_salary'] / info['count'] for season, info in season_totals.items()}

# Mostrar los salarios promedio por temporada
for season, average_salary in average_salaries.items():
    print(f'Temporada {season} - Salario promedio: ${average_salary:,.2f}')
