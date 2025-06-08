Démarrage rapide
=================

Étapes d'installation
---------------------

.. code-block:: bash

   git clone https://github.com/votre-repo/ai-tornado-chaser.git
   cd ai-tornado-chaser
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

Exécution des modèles
---------------------

.. code-block:: bash

   # Entraînement trajectoire
   python src/training/train_trajectory.py
   
   # Prédiction
   python src/inference/predict.py