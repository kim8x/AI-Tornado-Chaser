Prédiction de durée
===================

Modèle XGBoost
--------------

.. code-block:: python

   from xgboost import XGBRegressor
   from sklearn.model_selection import GridSearchCV
   
   model = XGBRegressor(max_depth=6, learning_rate=0.1)
   param_grid = {
       'n_estimators': [50, 100, 200],
       'max_depth': [3, 6, 9]
   }
   grid_search = GridSearchCV(model, param_grid, cv=5)
   grid_search.fit(X_train, y_train)

Caractéristiques d'entrée
-------------------------
1. Intensité initiale
2. Position (lat, lon)
3. Pression atmosphérique
4. Vitesse du vent
5. Mois de formation

Performances
------------
* RMSE: 12.0442 heures
* MAE: 9.5165 heures
* Correction de biais: +48 heures