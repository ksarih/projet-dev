import requests
import pandas as pd

def fetch_bike_stations(api_url: str) -> dict:
    """
    Récupère les informations des stations de vélo depuis une API et retourne un dictionnaire.

    Args:
        api_url (str): L'URL de l'API contenant les données des stations.

    Returns:
        dict: Dictionnaire où les clés sont les identifiants des stations et les valeurs sont 
              des tuples (latitude, longitude).

    Raises:
        ValueError: Si la requête API échoue.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        stations_data = response.json()
    else:
        raise ValueError(f"Erreur lors de la récupération des données : {response.status_code}")

    stations = {}
    for station in stations_data:
        name = station['id'].split(':')[-1]  # Code de la station (exemple : 001)
        lat = station['location']['value']['coordinates'][1]
        lon = station['location']['value']['coordinates'][0]
        stations[name] = (lat, lon)
    return stations


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Charge un fichier CSV et retourne un DataFrame Pandas.

    Args:
        file_path (str): Chemin du fichier CSV.

    Returns:
        pd.DataFrame: Les données du fichier CSV sous forme de DataFrame.
    """
    return pd.read_csv(file_path)


def convert_dates(data: pd.DataFrame, date_columns: list) -> pd.DataFrame:
    """
    Convertit les colonnes de date spécifiées dans un DataFrame au format datetime.

    Args:
        data (pd.DataFrame): Le DataFrame contenant les colonnes à convertir.
        date_columns (list): Liste des noms des colonnes à convertir.

    Returns:
        pd.DataFrame: Le DataFrame avec les colonnes converties.
    """
    for column in date_columns:
        data[column] = pd.to_datetime(data[column])
    return data


def filter_data_by_date(data: pd.DataFrame, target_date: str) -> pd.DataFrame:
    """
    Filtre les données pour inclure uniquement les lignes où une date de départ ou de retour correspond.

    Args:
        data (pd.DataFrame): Le DataFrame contenant les données de trajets.
        target_date (str): La date cible au format "YYYY-MM-DD".

    Returns:
        pd.DataFrame: Le DataFrame filtré avec les trajets correspondant à la date.
    """
    target_date = pd.to_datetime(target_date).date()
    return data[(data['Departure'].dt.date == target_date) | 
                (data['Return'].dt.date == target_date)]


# Exécution principale
if _name_ == "_main_":
    # Récupération des stations de vélo
    API_URL = 'https://portail-api-data.montpellier3m.fr/bikestation?limit=1000'
    try:
        bike_stations = fetch_bike_stations(API_URL)
        print("Stations de vélo récupérées :", bike_stations)
    except ValueError as e:
        print(e)
    
    # Chargement et traitement des données CSV
    CSV_FILE_PATH = 'data/TAM_MMM_CoursesVelomagg.csv'
    data = load_csv(CSV_FILE_PATH)

    # Conversion des colonnes de dates
    data = convert_dates(data, ['Departure', 'Return'])

    # Filtrage des données pour une date spécifique
    filtered_data = filter_data_by_date(data, '2024-09-30')
    print("Données filtrées pour le 30 septembre 2024 :")
    print(filtered_data)
