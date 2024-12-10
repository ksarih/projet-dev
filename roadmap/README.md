# Analyse et Visualisation du Trafic Cycliste à Montpellier 

## Introduction  
À Montpellier, le vélo est une option de transport écologique et populaire. Ce projet se concentre sur l'analyse et la visualisation du trafic cycliste dans la ville. Les objectifs incluent :  
- Prévoir les flux cyclistes à partir des données historiques.  
- Fournir des visualisations interactives pour une exploration approfondie.  
- Offrir des données en temps réel sur les vélos disponibles et les trajets cyclistes.  

L'ensemble des résultats et des outils est accessible sur notre site web, permettant aux utilisateurs d'explorer et de comprendre les déplacements à vélo.  

👉 Consultez la page principale : [site web](https://lucinebonnefont.github.io/projet-dev/)  
👉 Consultez la documentation complète : [Documentation détaillée](documentation/??????)  

---

## Objectifs du Projet  
- **Analyse du trafic cycliste** : Étudier les flux de vélos et identifier les tendances principales.  
- **Prévisions et prédictions** : Anticiper le trafic pour améliorer la planification des trajets.  
- **Disponibilité des vélos en temps réel** : Informer les utilisateurs sur la disponibilité des vélos Vélomagg dans la ville.  
- **Cartographie interactive** : Intégrer des outils interactifs comme **Leaflet.js** pour une exploration visuelle intuitive.  

## Données Exploitées

Notre site exploite des données ouvertes fournies par la Métropole de Montpellier pour vous offrir des outils interactifs et simplifier vos déplacements à vélo. Voici les jeux de données que nous utilisons :

### 1. Trajets réalisés par les vélos VéloMagg  
**Lien : [Courses des vélos VéloMagg de Montpellier Méditerranée Métropole](https://data.montpellier3m.fr/dataset/courses-des-velos-velomagg)**  

Ces données recensent les trajets effectués entre les stations VéloMagg depuis mai 2021. Elles nous permettent de :  
- Cartographier les itinéraires les plus fréquentés.  
- Analyser les tendances et horaires des déplacements.  
- Proposer des prévisions de trafic pour optimiser vos trajets.  

### 2. Comptages des vélos et piétons par éco-compteurs  
**Lien : [Comptages des vélos et piétons issus des compteurs de vélo](https://data.montpellier3m.fr/dataset/comptages-des-velos-et-pietons)**  

Ces données proviennent des éco-compteurs installés à des points stratégiques de la Métropole. Elles enregistrent :  
- Les passages horaires des vélos (et parfois des piétons).  
- Les tendances de trafic, avec des mises à jour quotidiennes.  

Elles nous aident à :  
- Identifier les zones les plus fréquentées.  
- Recommander des itinéraires pour éviter les trajets surchargés.  

### 3. Disponibilité des stations VéloMagg en temps réel  
**Lien : [Disponibilité des places VéloMagg en temps réel](https://data.montpellier3m.fr/dataset/disponibilite-des-velos-et-des-places-en-station)**  

Cette API fournit des informations actualisées sur :  
- Le nombre de vélos disponibles dans chaque station.  
- Le nombre de places libres pour y déposer un vélo.  

Elle nous permet de :  
- Afficher en temps réel les stations à proximité avec des vélos ou des places libres.  
- Simplifier la planification de vos trajets.  

### 4. Cartographie OpenStreetMap  
**Lien : [Cartographie OpenStreetMap](https://www.openstreetmap.org/#map=11/43.6045/3.9201)**  

Nous utilisons les données géographiques d’OpenStreetMap pour générer des cartes interactives et :  
- Visualiser les trajets des cyclistes dans la Métropole.  
- Délimiter des zones spécifiques
- Identifier les points d’intérêt et les stations VéloMagg sur les cartes.
  
---

## Architecture du Projet 

```python 

├── .github/workflows/
│     ├── deploy.yml
│     ├── update_bikes_dispos.yml
│     └── update_simulations.yml
├── data/
│     ├── MMM_MMM_GeolocCompteurs.csv
│     └── TAM_MMM_CoursesVelomagg.csv
├── docs/
│     ├── cache/
│     │     └── Commit changes before pull from remote
│     ├── data/
│     │     ├── 6_2022.json
│     │     ├── 6_2024.json
│     │     ├── MMM_MMM_GeolocCompteurs.csv
│     │     ├── TAM_MMM_CoursesVelomagg.csv
│     │     └── VilleMTP_MTP_Quartiers.json
│     ├── images/
│     │     ├── fontaine-place-comedie-montpellier.webp
│     │     └── logo.png
│     ├── site_libs/
│     │     └── page d'accueil
│     ├── styles/
│     │     └── custom.css
│     ├── .gitignore
│     ├── OCP.html
│     ├── _quarto.yml
│     ├── license.html
│     ├── bike_data.py
│     ├── compteurs.py
│     ├── density.html
│     ├── density.py
│     ├── density.qmd
│     ├── dispo.html
│     ├── dispo.qmd
│     ├── donnees.html
│     ├── donnees.qmd
│     ├── etude.html
│     ├── etude.qmd
│     ├── graphe_velib.py
│     ├── index.html
│     ├── index.qmd
│     ├── intensite_traffics_map.png
│     ├── license.qmd
│     ├── previsions.py
│     ├── search.json
│     ├── simulation.py
│     ├── trafic.html
│     ├── trafic.ipynb
│     └── trafic.qmd
├── documentation/
│     ├── source/
│     │     └── ajout du sphinx ext
│     ├── Makefile
│     ├── make.bat
├── previsions/
│     ├── prevision 01-05-2024.html
│     ├── prevision 14-11-2024.html
│     ├── prevision 25-12-2024.html
│     ├── reel 01-05-2024.html
│     └── reel 14-11-2024.html
├── roadmap/
│     ├── README.qmd
│     └── diagramme.md
├── .Rhistory
├── .gitignore
├── fetch_data.py
├── import_data.py
├── import_data2.py
├── import_data3.py
├── index.html
├── requirements.txt
└── telechargement_json.py
```

---

## Technologies Utilisées

### Langages et Frameworks :  
- **Python** : Analyse de données et modèles prédictifs.  
- **Quarto** : Génération du site Web interactif.  
- **JavaScript (Leaflet.js)** : Cartes interactives.  

### Bibliothèques Python :  
- **Pandas** : Nettoyage et manipulation des données.  
- **Seaborn** et **Matplotlib** : Visualisation des données.  
- **Folium** : Création de cartes interactives.  
- **Pooch** : Gestion des téléchargements de données.  

### Hébergement et Documentation :  
- **GitHub Pages** : Hébergement du site Web.  
- **Sphinx** : Documentation technique du projet.  

---

## Répartition des Tâches 

- **Gestion des données** : Import, nettoyage et analyse des bases de données.
- **Diagramme de Gantt** : Planification et suivi des étapes clés du projet.  
- **Cartographie interactive** : Génération de cartes dynamiques pour représenter les flux.  
- **Création du site Web** : Développement avec Quarto et intégration des résultats.  

---

## Licence
Ce projet est sous licence **MIT**.  
Consultez les détails ici : [Licence MIT](https://opensource.org/licenses/MIT).  

---

## Auteurs  
- **Lucine Bonnefont** 
- **Kaoutar Sarih**
- **Kilian Saint-Chély**
- **Naima Radouan**  
