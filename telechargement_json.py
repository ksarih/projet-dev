import pooch
import json

# URLs des fichiers .json
url_1 = "https://data.montpellier3m.fr/dataset/comptages-velo-et-pieton-issus-des-compteurs-de-velo"
url_2 = "https://data.montpellier3m.fr/dataset/quartiers-de-montpellier/resource/e6d5ead1-2f25-414d-9484-2971e7367fd8"

# Fichiers associés aux URLs
file_1_1 = "6_2022.json"
file_1_2 = "6_2024.json"
file_2 = "VilleMTP_MTP_Quartiers.json"

# Création d'un gestionnaire de cache pour télécharger et gérer les fichiers
cache = pooch.create(
    path=pooch.os_cache("mon_package"),  # Dossier de cache
    version="1.0.0",  # Version des fichiers
)

file_path_1_1 = cache.fetch(file_1_1)  # Télécharge 6_2022.json si pas déjà en cache
file_path_1_2 = cache.fetch(file_1_2)  # Télécharge 6_2024.json si pas déjà en cache
file_path_2 = cache.fetch(file_2)      # Télécharge VilleMTP_MTP_Quartiers.json si pas déjà en cache

# Charger les contenus des fichiers .json téléchargés
with open(file_path_1_1, "r") as f1_1:
    data_1_1 = json.load(f1_1)

with open(file_path_1_2, "r") as f1_2:
    data_1_2 = json.load(f1_2)

with open(file_path_2, "r") as f2:
    data_2 = json.load(f2)

# Afficher les données JSON
print("Contenu du fichier 6_2022.json :")
print(data_1_1)

print("Contenu du fichier 6_2024.json :")
print(data_1_2)

print("Contenu du fichier VilleMTP_MTP_Quartiers.json :")
print(data_2)
"""
Ce script télécharge des fichiers JSON à partir de deux URLs spécifiées, les sauvegarde dans un cache local,
et charge ensuite leur contenu pour pouvoir l'utiliser.

Les fichiers JSON sont :
- 6_2022.json et 6_2024.json qui contiennent des données sur les comptages de vélos et de piétons.
- VilleMTP_MTP_Quartiers.json qui contient des informations sur les quartiers de la ville de Montpellier.

Le script utilise la bibliothèque `pooch` pour gérer le cache des fichiers téléchargés.
Les données sont ensuite lues et affichées à l'écran.

URLs des fichiers :
- url_1 : Comptages de vélos et de piétons
- url_2 : Quartiers de la ville de Montpellier

Le cache est configuré pour stocker les fichiers dans un répertoire spécifique et garantir que les fichiers ne soient téléchargés qu'une seule fois.
"""

