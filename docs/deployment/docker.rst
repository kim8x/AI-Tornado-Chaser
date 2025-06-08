Déploiement Docker
===================

Fichier Dockerfile
------------------

.. code-block:: dockerfile

   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501 8000
   CMD ["streamlit", "run", "app.py"]

Construction et exécution
-------------------------

.. code-block:: bash

   docker build -t ai-tornado-chaser .
   docker run -p 8501:8501 -p 8000:8000 ai-tornado-chaser