"""
Ce script charge un fichier JSON contenant des données sur les vélos dans la ville de Montpellier,
y compris les informations sur les intensités et les dates des comptages, puis extrait les coordonnées géographiques (latitude et longitude).
Les données sont ensuite converties en un GeoDataFrame afin de pouvoir être manipulées géographiquement.

Le fichier JSON doit être structuré de manière à contenir une clé 'location' avec un sous-élément 'coordinates' qui contient un tableau de deux éléments :
- Longitude (premier élément)
- Latitude (deuxième élément)

Le résultat final est un GeoDataFrame contenant les informations de latitude, de longitude et les autres données associées, ainsi que la géométrie des points.

Étapes :
1. Charger le fichier JSON contenant les données de comptages de vélos.
2. Extraire les coordonnées géographiques (longitude et latitude).
3. Créer une colonne 'geometry' avec des objets `Point` pour les coordonnées.
4. Convertir le DataFrame en un GeoDataFrame avec le système de coordonnées de référence (CRS) du GeoDataFrame des quartiers de la ville de Montpellier.
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Charger les données de vélo avec les intensités et dates
df_velo = pd.read_json('data/VilleMTP_MTP_Quartiers.json')

# Extraire les coordonnées de latitude et longitude des points
df_velo['longitude'] = df_velo['location'].apply(lambda x: x['coordinates'][0])
df_velo['latitude'] = df_velo['location'].apply(lambda x: x['coordinates'][1])

# Créer la colonne geometry pour le GeoDataFrame
geometry = [Point(xy) for xy in zip(df_velo['longitude'], df_velo['latitude'])]

# Créer un GeoDataFrame à partir des données
gdf_velo = gpd.GeoDataFrame(df_velo, geometry=geometry, crs=quartiers_gdf.crs)

