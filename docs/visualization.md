# 📊 Guide de Visualisation et Analyses

## Visualisation des Trajectoires

### 1. Carte Interactive

```python
from cyclone_viz import CycloneMap

# Créer une carte interactive
cmap = CycloneMap()

# Ajouter une trajectoire
cmap.add_trajectory(
    coordinates,
    color='blue',
    width=2,
    opacity=0.8
)

# Ajouter une prédiction avec intervalle de confiance
cmap.add_prediction(
    prediction,
    confidence_interval=0.95,
    color='red'
)

# Afficher la carte
cmap.show()
```

### 2. Analyses Statistiques

```python
from cyclone_analytics import CycloneAnalytics

# Initialiser l'analyseur
analyzer = CycloneAnalytics(data)

# Statistiques descriptives
stats = analyzer.get_statistics()
```

## Types de Visualisations

### 1. Cartes de Chaleur
```python
def plot_density_map(data, region):
    """
    Crée une carte de densité des trajectoires de cyclones
    """
    plt.figure(figsize=(15, 10))
    
    # Configuration de la carte
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    
    # Tracer la densité
    sns.kdeplot(
        data=data,
        x='longitude',
        y='latitude',
        cmap='YlOrRd',
        fill=True
    )
    
    plt.title(f'Densité des Trajectoires - {region}')
    plt.show()
```

### 2. Séries Temporelles
```python
def plot_intensity_timeline(cyclone_data):
    """
    Visualise l'évolution de l'intensité du cyclone
    """
    plt.figure(figsize=(12, 6))
    
    plt.plot(
        cyclone_data['timestamp'],
        cyclone_data['intensity'],
        'b-',
        label='Intensité'
    )
    
    plt.fill_between(
        cyclone_data['timestamp'],
        cyclone_data['intensity_low'],
        cyclone_data['intensity_high'],
        alpha=0.2
    )
    
    plt.title('Évolution de l\'Intensité du Cyclone')
    plt.xlabel('Temps')
    plt.ylabel('Intensité (m/s)')
    plt.grid(True)
    plt.legend()
```

### 3. Diagrammes Polaires
```python
def plot_direction_distribution(data):
    """
    Crée un diagramme polaire des directions des cyclones
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    ax.hist(
        data['direction'],
        bins=36,
        range=(0, 2*np.pi)
    )
    
    plt.title('Distribution des Directions')
```

## Analyses Avancées

### 1. Clustering de Trajectoires
```python
from sklearn.cluster import DBSCAN

def cluster_trajectories(trajectories, eps=0.3, min_samples=5):
    """
    Regroupe les trajectoires similaires
    """
    clustering = DBSCAN(
        eps=eps,
        min_samples=min_samples,
        metric='haversine'
    ).fit(trajectories)
    
    return clustering.labels_
```

### 2. Analyse des Anomalies
```python
def detect_anomalies(trajectory):
    """
    Détecte les points inhabituels dans une trajectoire
    """
    model = IsolationForest(contamination=0.1)
    anomalies = model.fit_predict(trajectory)
    return anomalies
```

### 3. Métriques de Performance
```python
def calculate_metrics(real, predicted):
    """
    Calcule les métriques de performance du modèle
    """
    return {
        'mae': mean_absolute_error(real, predicted),
        'rmse': np.sqrt(mean_squared_error(real, predicted)),
        'r2': r2_score(real, predicted)
    }
```

## Rapports Automatiques

### 1. Génération de Rapports PDF
```python
from reportlab.pdfgen import canvas

def generate_report(cyclone_data, output_path):
    """
    Génère un rapport PDF détaillé
    """
    c = canvas.Canvas(output_path)
    
    # En-tête
    c.drawString(100, 750, "Rapport d'Analyse de Cyclone")
    
    # Ajouter des graphiques
    c.drawImage('trajectory.png', 100, 500, width=400, height=300)
    
    # Statistiques
    stats = calculate_statistics(cyclone_data)
    y = 450
    for key, value in stats.items():
        c.drawString(100, y, f"{key}: {value}")
        y -= 20
    
    c.save()
```

### 2. Exports de Données
```python
def export_analysis(data, format='csv'):
    """
    Exporte les résultats d'analyse
    """
    if format == 'csv':
        data.to_csv('analysis_results.csv')
    elif format == 'json':
        data.to_json('analysis_results.json')
    elif format == 'excel':
        data.to_excel('analysis_results.xlsx')
```

## Configuration des Visualisations

```python
# Configuration matplotlib
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.grid'] = True

# Configuration seaborn
sns.set_style("whitegrid")
sns.set_palette("husl")

# Configuration des cartes
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def setup_map():
    """
    Configure une carte basique
    """
    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes(projection=ccrs.PlateCarree())
    
    # Ajouter les caractéristiques de la carte
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.gridlines()
    
    return fig, ax
```

## Exemples d'Utilisation

### 1. Analyse Complète
```python
# Charger les données
data = load_cyclone_data('data/cyclones.csv')

# Créer les visualisations
plot_density_map(data, 'Pacifique Nord')
plot_intensity_timeline(data)
plot_direction_distribution(data)

# Analyser les trajectoires
clusters = cluster_trajectories(data['trajectories'])
anomalies = detect_anomalies(data['trajectories'])

# Générer le rapport
generate_report(data, 'rapport_cyclone.pdf')
```

### 2. Dashboard Interactif
```python
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='trajectory-map'),
    dcc.Graph(id='intensity-graph'),
    dcc.Graph(id='direction-rose'),
    html.Div([
        html.H4('Statistiques'),
        html.Table(id='stats-table')
    ])
])

# Callbacks pour l'interactivité
@app.callback(
    Output('trajectory-map', 'figure'),
    [Input('date-picker', 'value')]
)
def update_map(date):
    # Mettre à jour la carte
    pass
```
