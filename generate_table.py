import pandas as pd

# Chemin vers le fichier de données
data_path = "projet/TAM_MMM_CoursesVelomagg .csv"

# Charger les données et ne garder que les colonnes qui nous intéressent
df = pd.read_csv(data_path)
df = df[['Departure', 'Return', 'Departure station', 'Return station', 'Covered distance (m)', 'Duration (sec.)']]

# Optionnel : Calculer les 10 trajets les plus fréquents ou longs, par exemple
# On peut aussi trier par la distance parcourue pour montrer les plus longs trajets
top_trajets = df.sort_values(by='Covered distance (m)', ascending=False).head(10)

# Générer le tableau HTML et l'enregistrer dans le dossier docs
top_trajets_html = top_trajets.to_html(index=False)
output_path = "docs/flux_velo_montpellier.html"
with open(output_path, "w") as file:
    file.write(top_trajets_html)

print(f"Tableau HTML généré dans {output_path}")
