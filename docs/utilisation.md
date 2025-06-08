# Guide d'Utilisation

## Traitement des Données

### 1. Extraction des Données

Pour extraire les données des fichiers `.txt` en format CSV :

```python
from scripts.extract_to_csv import extract_cyclone_data

# Extraire les données
extract_cyclone_data('data/raw/', 'data/processed/cyclones.csv')
```

### 2. Transformation des Coordonnées

Pour convertir les coordonnées géographiques en coordonnées polaires :

```python
from scripts.geodesic_utils import compute_stepwise

# Exemple de trajectoire
trajectoire = [(23.4, 120.5), (23.6, 120.7), (23.9, 121.0)]
etapes = compute_stepwise(trajectoire)
```

### 3. Normalisation des Données

Deux approches de normalisation sont disponibles :

#### Normalisation Locale (par cyclone)
```python
def normaliser_local(trajectoire):
    lat, lon = zip(*trajectoire)
    lat_norm = (lat - np.mean(lat)) / np.std(lat)
    lon_norm = (lon - np.mean(lon)) / np.std(lon)
    return list(zip(lat_norm, lon_norm))
```

#### Normalisation Globale
```python
def normaliser_global(trajectoire, lat_min, lat_max, lon_min, lon_max):
    lat, lon = zip(*trajectoire)
    lat_norm = (lat - lat_min) / (lat_max - lat_min)
    lon_norm = (lon - lon_min) / (lon_max - lon_min)
    return list(zip(lat_norm, lon_norm))
```

## Modélisation

### 1. Modèle Conjoint

Pour prédire la latitude et la longitude ensemble :

```python
from models.model_lat_lon import CycloneTrajectoryModel

model = CycloneTrajectoryModel()
model.train(X_train, y_train)
predictions = model.predict(X_test)
```

### 2. Modèles Séparés

Pour des prédictions séparées de latitude et longitude :

```python
from models.model_separate import LatitudeModel, LongitudeModel

lat_model = LatitudeModel()
lon_model = LongitudeModel()

lat_model.train(X_train, y_train_lat)
lon_model.train(X_train, y_train_lon)

lat_pred = lat_model.predict(X_test)
lon_pred = lon_model.predict(X_test)
```

## Visualisation

### 1. Tracer les Trajectoires

```python
import matplotlib.pyplot as plt

def tracer_trajectoire(trajectoire_reelle, trajectoire_predite):
    plt.figure(figsize=(10, 6))
    lat_r, lon_r = zip(*trajectoire_reelle)
    lat_p, lon_p = zip(*trajectoire_predite)
    
    plt.plot(lon_r, lat_r, 'b-', label='Trajectoire Réelle')
    plt.plot(lon_p, lat_p, 'r--', label='Trajectoire Prédite')
    
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid(True)
    plt.show()
```

### 2. Analyse d'Erreur

```python
def calculer_erreur(trajectoire_reelle, trajectoire_predite):
    from geographiclib.geodesic import Geodesic
    
    erreurs = []
    for (lat_r, lon_r), (lat_p, lon_p) in zip(trajectoire_reelle, trajectoire_predite):
        distance = Geodesic.WGS84.Inverse(lat_r, lon_r, lat_p, lon_p)['s12']
        erreurs.append(distance)
    
    return {
        'erreur_moyenne': np.mean(erreurs),
        'erreur_max': np.max(erreurs),
        'erreur_std': np.std(erreurs)
    }
```
