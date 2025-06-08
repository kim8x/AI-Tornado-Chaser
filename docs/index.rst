# Tropical-Cyclone-chasers

## 📊 Description du Dataset

- **Format**: Chaque fichier `.txt` contient plusieurs enregistrements de cyclones, chacun commençant par un en-tête suivi d'un ou plusieurs points de trajectoire.
- **Champs extraits**:
  - `cyclone_id`
  - `date` et `time`
  - `LAT`, `LON` (dixièmes de degrés)
  - Optionnel: `vitesse_du_vent`, `pression`

- **Système de coordonnées**:
  - Latitude et Longitude sont données en **dixièmes de degrés** (ex: 216 → 21.6°N)
  - Transformées en **degrés décimaux** pour la modélisation
  - Ellipsoïde de référence: **WGS84**

## 🔧 Fonctionnalités Principales

- ✅ Analyse des trajectoires de cyclones à partir de fichiers `.txt` bruts
- ✅ Normalisation des trajectoires localement (par cyclone) ou globalement
- ✅ Conversion lat/lon en **coordonnées polaires par étapes** utilisant [GeographicLib](https://geographiclib.sourceforge.io/)
- ✅ Reconstruction des coordonnées à partir des étapes polaires pour l'analyse d'erreur
- ✅ Entraînement des modèles:
  - Prédiction de latitude & longitude **conjointement**
  - Prédiction de latitude et longitude avec **modèles séparés**

## 📁 Structure du Projet

```
data/
│ └── raw/ # Dossiers bruts de fichiers cyclone .txt (par année)
│
notebooks/
│ └── exploratory.ipynb # Exploration des données et logique de transformation
│
scripts/
│ └── extract_to_csv.py # Parse les fichiers .txt en format CSV
│ └── geodesic_utils.py # Calculs des étapes basés sur GeographicLib
│ └── reconstruction.py # Reconstruit la trajectoire à partir des coordonnées polaires
│
models/
│ └── model_lat_lon.py # Modèle prédisant lat & lon conjointement
│ └── model_separate.py # Modèles séparés pour lat et lon
```

## 🧪 Approches de Modélisation

- **Prédiction par étapes**: chaque point suivant est prédit par rapport au dernier, en utilisant la distance et le cap (géodésique).
- **Suivi des erreurs**: Les points reconstruits vs originaux sont comparés avec l'erreur du grand cercle (en mètres).
- **Stratégies de normalisation**:
  - Par trajectoire (échelle locale): préserve la variation
  - Échelle globale: normalisation fixe pour l'inférence

## 📈 Exemple d'Utilisation

```python
from geographiclib.geodesic import Geodesic
from geodesic_utils import compute_stepwise

trajectoire = [(23.4, 120.5), (23.6, 120.7), (23.9, 121.0)]
etapes = compute_stepwise(trajectoire)
# Sortie: [(2.76, 71.3), (3.58, 74.9)]  # (distance_km, cap_deg)
```

## Installation

1. Cloner le dépôt:
```bash
git clone https://github.com/votre-nom/Tropical-Cyclone-chasers.git
cd Tropical-Cyclone-chasers
```

2. Installer les dépendances:
```bash
pip install -r requirements.txt
```

## Configuration

1. Assurez-vous que vos fichiers de données sont placés dans le dossier `data/raw/`
2. Configurez les paramètres dans `config.yaml` si nécessaire

## Contribution

Les contributions sont les bienvenues! Veuillez:

1. Fork le projet
2. Créer votre branche de fonctionnalité
3. Commit vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request
