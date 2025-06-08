# Guide d'Installation

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Git

## Installation

1. Clonez le dépôt:
```bash
git clone https://github.com/votre-nom/Tropical-Cyclone-chasers.git
cd Tropical-Cyclone-chasers
```

2. Créez un environnement virtuel (recommandé):
```bash
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
.\venv\Scripts\activate  # Sur Windows
```

3. Installez les dépendances:
```bash
pip install -r requirements.txt
```

## Configuration

1. Placez vos fichiers de données dans le dossier `data/raw/`
2. Vérifiez que le format des fichiers correspond au format attendu (voir la section Format des Données)
3. Si nécessaire, ajustez les paramètres dans `config.yaml`

## Structure des Données

Les fichiers de données doivent être au format `.txt` avec la structure suivante:

```
CYCLONE_ID,DATE,TIME,LAT,LON[,WIND_SPEED,PRESSURE]
```

Exemple:
```
TC001,20250601,1200,216,-845,65,998
```

où:
- LAT et LON sont en dixièmes de degrés
- WIND_SPEED est en nœuds
- PRESSURE est en hPa

## Vérification de l'Installation

Pour vérifier que tout est correctement installé:

1. Lancez Python:
```python
from geodesic_utils import compute_stepwise
print("Installation réussie!")
```

2. Exécutez les tests:
```bash
python -m pytest tests/
```
