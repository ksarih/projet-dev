import numpy as np
import pandas as pd
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import osmnx as ox
 
data2 = pd.read_csv('MMM_MMM_GeolocCompteurs.csv')       # Chargement du Fichier CSV
# Conversion des Colonnes de Latitude et Longitude au Format Numérique
data2['Latitude'] = pd.to_numeric(data2['Latitude'], errors='coerce')
data2['Longitude'] = pd.to_numeric(data2['Longitude'], errors='coerce')


gdf = gpd.GeoDataFrame(
    data2, geometry=gpd.points_from_xy(data2.Longitude, data2.Latitude))

# Définition du Système de Coordonnées (WGS84)
gdf.set_crs(epsg=4326, inplace=True)

# Tracé des Points sur une Carte avec des Informations Supplémentaires
colors = plt.cm.rainbow(np.linspace(0, 1, len(gdf)))
fig, ax = plt.subplots(figsize=(15, 15))
gdf.plot(ax=ax, color='darkgreen', markersize=50)

# Créer une légende avec les noms des compteurs et le nombre de vélos disponibles
legend_labels = []
colors = ['blue'] * len(gdf)  # Create a list of colors matching the number of points

for i, (label, bikes) in enumerate(zip(gdf['Nom du com'], gdf['N° Série'])):
    ax.plot(gdf.geometry.x[i], gdf.geometry.y[i], 'o', color=colors[i], markersize=10)
    legend_labels.append(f"{label} ({bikes} vélos)")

handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
                      markersize=10, label=label) for label in legend_labels]
ax.legend(handles=handles, title="Compteurs de Vélo", loc='upper right', 
          bbox_to_anchor=(1.3, 1))

plt.title('Localisation des Compteurs de Vélo à Montpellier')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Ajouter une petite légende avec le graphe
plt.figtext(0.5, 0.01, 
            "Les points représentent les compteurs de vélo et leurs positions exactes dans la ville de Montpellier", 
            wrap=True, horizontalalignment='center', fontsize=12)

# Sauvegarder la figure dans un fichier
plt.savefig('figure_with_legend.png', bbox_inches='tight')
plt.show()

data2 = get_bike_data('2023-01-01')
plot_bike_data(data2)
