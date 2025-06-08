Déploiement du Chatbot
======================

Interface Streamlit
-------------------

.. code-block:: python

   import streamlit as st
   
   st.title("Assistant d'urgence pour ouragans")
   user_input = st.text_input("Posez votre question:")
   
   if user_input:
       response = get_response(user_input)
       st.write(f"**Réponse**: {response}")

Options de déploiement
----------------------
1. Local: ``streamlit run app.py``
2. Docker: Containerisation complète
3. Cloud: Déploiement sur AWS/GCP