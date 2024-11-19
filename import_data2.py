import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point

data2 = pd.read_csv('MMM_MMM_GeolocCompteurs.csv')
# Conversion des Col de Latitude et Long au Format Num
data2['Latitude'] = pd.to_numeric(data2['Latitude'], errors='coerce')
data2['Longitude'] = pd.to_numeric(data2['Longitude'], errors='coerce')
gdf = gpd.GeoDataFrame(
    data2, geometry=gpd.points_from_xy(data2.Longitude, data2.Latitude)
)
gdf.set_crs(epsg=4326, inplace=True)
# Tracé des Points sur une Carte avec des Informations Supplémentaires
fig, ax = plt.subplots(figsize=(8, 8))  # Réduire la taille du graphique
# Tracer les points avec des couleurs différentes
colors = plt.cm.rainbow(np.linspace(0, 1, len(gdf)))
scatter = ax.scatter(gdf.geometry.x, gdf.geometry.y, color=colors, s=50)
# Ajouter des infobulles pour afficher la légende lorsque la souris survole les points du graphique
annot = ax.annotate("", xy=(0,0), xytext=(20,20),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)
def update_annot(ind):
    pos = scatter.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = f"{gdf['Nom du com'].iloc[ind['ind'][0]]} ({gdf['N° Série'].iloc[ind['ind'][0]]} vélos)"
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor('lightblue')
    annot.get_bbox_patch().set_alpha(0.8)
def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = scatter.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()
fig.canvas.mpl_connect("motion_notify_event", hover)
plt.title('Localisation des Compteurs de Vélo à Montpellier')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.figtext(
    0.5, 0.01,
    "Les points représentent les compteurs de vélo et leurs positions exactes tout au long de Montpellier.",
    wrap=True, horizontalalignment='center', fontsize=12
)

# Sauvegarder la figure dans un fichier
plt.savefig('figure_with_tooltips.png', bbox_inches='tight')
# Afficher la carte avec infobulles
plt.show()

# Exemple de fonction pour récupérer et tracer des données supplémentaires (si définie)
def get_bike_data(date):
    # Exemple de fonction fictive pour obtenir des données
    return data2

def plot_bike_data(data):
    print(f"Tracé des données de vélo pour la date : {data}")

data2 = get_bike_data('2023-01-01')
plot_bike_data(data2)
