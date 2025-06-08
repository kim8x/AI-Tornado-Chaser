Description des données
=======================

Source des données
------------------
* **Centre de données**: CMA Tropical Cyclone Data Center
* **Période**: 1949-2023
* **Enregistrements**: 2 489 ouragans/typhons
* **Résolution temporelle**: 1 entrée toutes les 6 heures

Champs principaux
-----------------

.. list-table::
   :header-rows: 1
   
   * - Champ
     - Description
     - Format
   * - YYYYMMDDHH
     - Date et heure UTC
     - AAAAMMJJHH
   * - LAT
     - Latitude
     - 0.1°N
   * - LONG
     - Longitude
     - 0.1°E
   * - PRES
     - Pression minimale
     - hPa
   * - WND
     - Vitesse du vent max
     - m/s

Classification d'intensité
--------------------------

.. list-table::
   :header-rows: 1
   
   * - Catégorie
     - Désignation
     - Vitesse vent (m/s)
   * - 0
     - Inférieur à TD
     - -
   * - 1
     - Dépression tropicale (TD)
     - 10.8-17.1
   * - 4
     - Typhon (TY)
     - 32.7-41.4
   * - 6
     - Super Typhon
     - ≥51.0