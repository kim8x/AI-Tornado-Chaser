# Guide de Démarrage Rapide

## Installation Rapide

```bash
# Cloner le repository
git clone https://github.com/votre-nom/Tropical-Cyclone-chasers.git
cd Tropical-Cyclone-chasers

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Configuration Initiale

1. **Configuration de l'Environnement**
   ```yaml
   # config.yaml
   model:
     type: "bilstm"
     sequence_length: 10
     batch_size: 32
   
   data:
     input_dir: "data/raw"
     output_dir: "data/processed"
   
   api:
     host: "localhost"
     port: 5000
   ```

2. **Préparation des Données**
   ```bash
   python scripts/prepare_data.py --input data/raw --output data/processed
   ```

3. **Lancement de l'API**
   ```bash
   python api.py
   ```

## Premiers Pas

### 1. Prédiction Simple

```python
import requests

# Faire une prédiction
response = requests.post(
    "http://localhost:5000/predict",
    json={
        "coordinates": [
            {"lat": 23.4, "lon": 120.5},
            {"lat": 23.6, "lon": 120.7}
        ]
    }
)

print(response.json())
```

### 2. Utilisation du Chatbot

```python
from cyclone_bot import CycloneBot

bot = CycloneBot()

# Prédire une trajectoire
prediction = bot.predict("23.4N 120.5E")
print(prediction)

# Obtenir l'historique
history = bot.get_history("Pacifique Nord-Ouest")
print(history)
```

### 3. Visualisation Rapide

```python
from cyclone_viz import plot_trajectory

# Tracer une trajectoire
plot_trajectory(
    coordinates,
    prediction,
    title="Trajectoire du Cyclone",
    show_confidence=True
)
```

## Résolution des Problèmes Courants

### Erreur de Connexion API
```python
ConnectionError: Failed to connect to localhost:5000

Solution:
1. Vérifier que l'API est en cours d'exécution
2. Vérifier le pare-feu
3. Confirmer les paramètres dans config.yaml
```

### Erreur de Modèle
```python
ModelNotFoundError: Cannot find model at 'models/bilstm_model.h5'

Solution:
1. Exécuter l'entraînement du modèle
2. Vérifier le chemin du modèle dans config.yaml
```

### Problèmes de Mémoire
```
MemoryError: Cannot allocate memory

Solution:
1. Réduire batch_size dans config.yaml
2. Libérer la mémoire GPU
3. Augmenter la mémoire swap
```

## Prochaines Étapes

1. [Documentation Technique Complète](./technical.md)
2. [Guide du Développeur](./developer.md)
3. [Tutoriels Avancés](./tutorials.md)
4. [Guide de Contribution](./contributing.md)
