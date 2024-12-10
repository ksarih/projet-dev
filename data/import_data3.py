# Charger les données de vélo avec les intensités et dates
df_velo = pd.read_json(file_path)
# Extraire les coordonnées de latitude et longitude des points
df_velo['longitude'] = df_velo['location'].apply(lambda x: x['coordinates'][0])
df_velo['latitude'] = df_velo['location'].apply(lambda x: x['coordinates'][1])
# Créer la colonne geometry pour le GeoDataFrame
geometry = [Point(xy) for xy in zip(df_velo['longitude'], df_velo['latitude'])]
gdf_velo = gpd.GeoDataFrame(df_velo, geometry=geometry, crs=quartiers_gdf.crs)
