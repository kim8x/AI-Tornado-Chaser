Déploiement local
==================

Commandes de démarrage
----------------------

.. code-block:: bash

   # Application principale
   streamlit run app.py --server.port 8501
   
   # Service API
   uvicorn api.main:app --reload --port 8000

Accès
------
* Interface web: http://localhost:8501
* Documentation API: http://localhost:8000/docs