# Documentation de l'API

## Module extract_to_csv

### `extract_cyclone_data(input_dir: str, output_file: str) -> None`

Extrait les données de cyclones des fichiers texte et les sauvegarde en format CSV.

#### Paramètres:
- `input_dir` : Chemin vers le répertoire contenant les fichiers .txt
- `output_file` : Chemin pour le fichier CSV de sortie

## Module geodesic_utils

### `compute_stepwise(trajectory: List[Tuple[float, float]]) -> List[Tuple[float, float]]`

Calcule les étapes polaires (distance, cap) entre points consécutifs d'une trajectoire.

#### Paramètres:
- `trajectory` : Liste de tuples (latitude, longitude) en degrés décimaux

#### Retourne:
- Liste de tuples (distance_km, cap_degrés)

### `reconstruct_trajectory(start_point: Tuple[float, float], steps: List[Tuple[float, float]]) -> List[Tuple[float, float]]`

Reconstruit une trajectoire à partir d'un point de départ et d'étapes polaires.

#### Paramètres:
- `start_point` : Tuple (latitude, longitude) du point initial
- `steps` : Liste de tuples (distance_km, cap_degrés)

#### Retourne:
- Liste de tuples (latitude, longitude) reconstruits

## Module model_lat_lon

### class `CycloneTrajectoryModel`

Modèle pour prédire conjointement la latitude et la longitude.

#### Méthodes:

##### `__init__(hidden_size: int = 128)`
Initialise le modèle.

##### `train(X: np.ndarray, y: np.ndarray) -> None`
Entraîne le modèle.

- `X` : Features d'entrée
- `y` : Valeurs cibles (lat, lon)

##### `predict(X: np.ndarray) -> np.ndarray`
Fait des prédictions.

- `X` : Features d'entrée
- Retourne: Prédictions (lat, lon)

## Module model_separate

### class `LatitudeModel`

Modèle spécialisé pour la prédiction de latitude.

### class `LongitudeModel`

Modèle spécialisé pour la prédiction de longitude.

Ces deux classes suivent la même interface que `CycloneTrajectoryModel` mais sont
optimisées pour leur composante respective.

## Module reconstruction

### `calculate_error(real: List[Tuple[float, float]], predicted: List[Tuple[float, float]]) -> Dict[str, float]`

Calcule les métriques d'erreur entre trajectoires réelle et prédite.

#### Paramètres:
- `real` : Liste de tuples (lat, lon) réels
- `predicted` : Liste de tuples (lat, lon) prédits

#### Retourne:
Dictionary contenant:
- `erreur_moyenne` : Erreur moyenne en km
- `erreur_max` : Erreur maximale en km
- `erreur_std` : Écart-type des erreurs
