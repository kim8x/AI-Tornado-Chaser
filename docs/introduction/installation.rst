Installation et configuration
=============================

Prérequis
---------

.. code-block:: bash

   # Python 3.8+
   python --version
   
   # Paquets système
   sudo apt-get update
   sudo apt-get install python3-pip python3-venv

Configuration de l'environnement
--------------------------------

.. code-block:: bash

   # Créer environnement virtuel
   python -m venv tornado_chaser_env
   source tornado_chaser_env/bin/activate  # Linux/Mac
   .\tornado_chaser_env\Scripts\activate  # Windows

   # Installer les dépendances
   pip install -r requirements.txt

Dépendances principales
-----------------------

.. list-table::
   :header-rows: 1
   
   * - Paquet
     - Version
   * - tensorflow
     - >=2.8.0
   * - xgboost
     - >=1.5.0
   * - streamlit
     - >=1.20.0
   * - sentence-transformers
     - >=2.2.0
     