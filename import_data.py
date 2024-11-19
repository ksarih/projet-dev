import requests
import pandas as pd

# Récupérer les données de l'API : bikestation
url = 'https://portail-api-data.montpellier3m.fr/bikestation?limit=1000'
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    stations_data = response.json()  # Parse le JSON
else:
    print(f"Erreur lors de la récupération des données : {response.status_code}")

# Extraire les informations de localisation des stations
stations = {}
for station in stations_data:
    name = station['id'].split(':')[-1] # Code de la station (001)
    lat = station['location']['value']['coordinates'][1] 
    lon = station['location']['value']['coordinates'][0]
    stations[name] = (lat, lon)

print(stations)

# Charger le fichier CSV
data = pd.read_csv('data/TAM_MMM_CoursesVelomagg.csv')

# Convertir les colonnes de date au format datetime
data['Departure'] = pd.to_datetime(data['Departure'])
data['Return'] = pd.to_datetime(data['Return'])

# Filtrer pour le 30 septembre 2024
filtered_data = data[(data['Departure'].dt.date == pd.to_datetime('2024-09-30').date()) |
                     (data['Return'].dt.date == pd.to_datetime('2024-09-30').date())]

print(filtered_data)