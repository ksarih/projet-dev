import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import folium

# Charger les données des quartiers (GeoJSON ou shapefile)
quartiers_gdf = gpd.read_file('data/VilleMTP_MTP_Quartiers.json')

def calculer_intensite_moyenne(file_path, quartiers_gdf):
    """
    Fonction pour calculer l'intensité moyenne des stations de vélos par quartier
    et par date.

    Cette fonction charge un fichier JSON contenant des données sur les stations de vélos,
    calcule l'intensité moyenne des trajets observés pour chaque quartier de la ville
    et renvoie un GeoDataFrame des quartiers avec les intensités moyennes associées.

    Le fichier JSON doit être structuré de manière à contenir les informations de localisation
    des stations de vélo et une colonne 'dateObserved' pour la date des trajets, ainsi qu'une colonne
    'intensity' pour l'intensité de chaque trajet.

    Paramètres :
    - file_path (str) : Chemin vers le fichier JSON contenant les données des stations de vélos.
    - quartiers_gdf (GeoDataFrame) : GeoDataFrame des quartiers de la ville avec la géométrie et les informations associées.

    Retourne :
    - GeoDataFrame : Un GeoDataFrame des quartiers avec une nouvelle colonne 'intensity' indiquant l'intensité
      moyenne des trajets de vélo observés dans chaque quartier.
    """
    
    # Charger les données de vélo avec les intensités et dates
    df_velo = pd.read_json(file_path)

    # Extraire les coordonnées de latitude et longitude des points
    df_velo['longitude'] = df_velo['location'].apply(lambda x: x['coordinates'][0])
    df_velo['latitude'] = df_velo['location'].apply(lambda x: x['coordinates'][1])

    # Créer la colonne geometry pour le GeoDataFrame
    geometry = [Point(xy) for xy in zip(df_velo['longitude'], df_velo['latitude'])]
    gdf_velo = gpd.GeoDataFrame(df_velo, geometry=geometry, crs=quartiers_gdf.crs)

    # Associer les points de vélo aux quartiers
    gdf_joined = gpd.sjoin(gdf_velo, quartiers_gdf, how="inner", predicate="intersects")

    # Calculer la moyenne journalière par quartier et par date
    gdf_joined['start_date'] = gdf_joined['dateObserved'].apply(lambda x: x.split('/')[0])
    gdf_joined['start_date'] = pd.to_datetime(gdf_joined['start_date'])

    moyennes_quartiers = (
        gdf_joined.groupby(['name', 'start_date'])
        .agg({'intensity': 'mean'})
        .reset_index()
    )

    # Fusionner avec les données des quartiers pour les visualisations
    return quartiers_gdf.merge(
        moyennes_quartiers.groupby('name').agg({'intensity': 'mean'}).reset_index(),
        on='name',
        how='left'
    )


# Calculer les intensités pour 2022 et 2024
quartiers_gdf_2022 = calculer_intensite_moyenne('data/6_2022.json', quartiers_gdf.copy())
quartiers_gdf_2024 = calculer_intensite_moyenne('data/6_2024.json', quartiers_gdf.copy())

# Préparer les données pour Folium
quartiers_gdf_2022['intensity'] = quartiers_gdf_2022['intensity'].fillna(0)  # Remplacer les NaN par 0
quartiers_gdf_2024['intensity'] = quartiers_gdf_2024['intensity'].fillna(0)

# Créer une carte Folium pour 2022
m_2022 = folium.Map(location=[43.610769, 3.876716], zoom_start=12, tiles="CartoDB positron")

# Ajouter les quartiers avec des intensités en 2022
for _, row in quartiers_gdf_2022.iterrows():
    style = {
        'fillColor': 'red',
        'color': 'black',
        'weight': 1,
        'fillOpacity': row['intensity'] / quartiers_gdf_2022['intensity'].max()  # Échelle d'opacité
    }
    folium.GeoJson(
        row['geometry'].__geo_interface__,
        style_function=lambda x, style=style: style
    ).add_to(m_2022)

# Ajouter des étiquettes de noms de quartiers
for _, row in quartiers_gdf_2022.iterrows():
    folium.Marker(
        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
        popup=f"{row['name']}: {row['intensity']:.2f}"
    ).add_to(m_2022)

# Enregistrer la carte sous forme de fichier HTML
m_2022.save("intensite_2022.html")

# Créer une carte Folium pour 2024 (facultatif, similaire à 2022)
m_2024 = folium.Map(location=[43.610769, 3.876716], zoom_start=12, tiles="CartoDB positron")
for _, row in quartiers_gdf_2024.iterrows():
    style = {
        'fillColor': 'blue',
        'color': 'black',
        'weight': 1,
        'fillOpacity': row['intensity'] / quartiers_gdf_2024['intensity'].max()
    }
    folium.GeoJson(
        row['geometry'].__geo_interface__,
        style_function=lambda x, style=style: style
    ).add_to(m_2024)
for _, row in quartiers_gdf_2024.iterrows():
    folium.Marker(
        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
        popup=f"{row['name']}: {row['intensity']:.2f}"
    ).add_to(m_2024)
m_2024.save("intensite_2024.html")
