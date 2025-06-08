# Documentation des Notebooks

## Vue d'ensemble des Notebooks

Le projet utilise plusieurs notebooks Jupyter pour l'analyse et le développement:

### 1. `final_times_series_project.ipynb`

Notebook principal contenant:
- Prétraitement des données cycloniques
- Développement des modèles de séries temporelles
- Évaluation des performances

#### Fonctionnalités principales:
- Chargement et nettoyage des données
- Normalisation des coordonnées (latitude/longitude)
- Création de séquences pour l'apprentissage
- Implémentation de différents modèles (LSTM, GRU, BiLSTM)
- Visualisation des résultats

### 2. `API.ipynb`

Notebook d'implémentation de l'API contenant:
- Configuration du serveur Flask
- Points d'accès pour les prédictions
- Gestion des requêtes

#### Points d'accès API:

```python
POST /predict
{
    "input": [[lat1, lon1], [lat2, lon2], ...]  # Séquence de points
}
```

Réponse:
```python
{
    "sequence": [[lat_pred1, lon_pred1], ...]  # Prédictions
}
```

### 3. `time_series_model_1.ipynb`

Notebook d'expérimentation contenant:
- Tests de différentes architectures
- Optimisation des hyperparamètres
- Analyses comparatives

## Interface Chatbot

Le projet inclut une interface chatbot qui permet:

### Fonctionnalités du Chatbot:

1. **Requêtes en Langage Naturel**
   - Interrogation sur les trajectoires des cyclones
   - Demandes de prédictions
   - Questions sur les données historiques

2. **Commandes Disponibles**:
   ```
   /predict <coordonnées> - Prédit la trajectoire future
   /history <région> - Affiche l'historique des cyclones
   /risk <coordonnées> - Évalue le risque cyclonique
   ```

3. **Exemples d'Utilisation**:
   ```python
   # Prédiction de trajectoire
   chatbot.predict("23.4N 120.5E")
   
   # Historique des cyclones
   chatbot.get_history("Pacifique Nord-Ouest")
   ```

### Intégration API:

Le chatbot utilise l'API REST pour:
1. Obtenir des prédictions en temps réel
2. Accéder aux données historiques
3. Générer des visualisations

### Configuration du Chatbot:

```python
from cyclone_chatbot import CycloneBot

bot = CycloneBot(
    api_url="http://localhost:5000",
    model_path="models/bilstm_model.h5",
    language="fr"
)
```

### Personnalisation:

Le chatbot peut être configuré pour:
- Différentes langues (FR/EN)
- Différents formats de coordonnées
- Différents niveaux de détail dans les réponses

## Modèles de Deep Learning

### BiLSTM (Modèle Principal)

Architecture:
```python
model = Sequential([
    Bidirectional(LSTM(128, return_sequences=True)),
    Dropout(0.2),
    Bidirectional(LSTM(64)),
    Dense(2)  # Prédiction [lat, lon]
])
```

### Entrainement:

```python
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='mse',
    metrics=['mae']
)

history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2
)
```

## Utilisation du Modèle via API

### Python:
```python
import requests

data = {
    "input": [[23.4, 120.5], [23.6, 120.7]]
}

response = requests.post(
    "http://localhost:5000/predict",
    json=data
)

predictions = response.json()["sequence"]
```

### cURL:
```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"input": [[23.4, 120.5], [23.6, 120.7]]}'
```
