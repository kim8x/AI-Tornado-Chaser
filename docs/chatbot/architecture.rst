Architecture du Chatbot
=======================

Sources de connaissances
------------------------
1. Communications sur les réseaux sociaux
2. Protocoles d'urgence FEMA
3. Contenu généré par ChatGPT

Implémentation technique
------------------------

.. code-block:: python

   from sentence_transformers import SentenceTransformer
   import faiss
   
   # Initialisation du modèle
   embedder = SentenceTransformer('all-MiniLM-L6-v2')
   
   # Création des embeddings
   question_embeddings = embedder.encode(questions)
   
   # Index FAISS
   index = faiss.IndexFlatIP(question_embeddings.shape[1])
   index.add(question_embeddings)

Exemple d'interaction
---------------------
**Utilisateur**: "Comment se préparer à un ouragan?"

**Chatbot**: "Commencez à préparer 72 heures avant la tempête. Stockez de l'eau (3.7L/personne/jour), de la nourriture non périssable..."