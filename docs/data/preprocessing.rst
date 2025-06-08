Prétraitement des données
=========================

Étapes de prétraitement
-----------------------
1. Nettoyage des données manquantes
2. Normalisation des caractéristiques
3. Création de séquences temporelles
4. Division train/validation/test

Normalisation
-------------
Deux stratégies comparées:

.. list-table::
   :header-rows: 1
   
   * - Méthode
     - Avantages
     - Inconvénients
   * - Globale
     - Simple
     - Aplatit les petites trajectoires
   * - **Par trajectoire**
     - **Meilleure adaptation locale**
     - **Complexe en inférence**

Exemple de code
---------------

.. code-block:: python

   import numpy as np
   from sklearn.preprocessing import MinMaxScaler
   
   def normalize_trajectory(data):
       scaler = MinMaxScaler()
       return scaler.fit_transform(data)