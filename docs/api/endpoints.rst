Points de terminaison API
=========================

Prédiction de trajectoire
-------------------------
**Endpoint**: ``/predict/trajectory``

Requête:
```json
{
  "sequence": [
    {"lat": 25.5, "lon": -80.0, "pressure": 980},
    {"lat": 25.7, "lon": -80.2, "pressure": 975}
  ]
}