Prédiction de trajectoire
=========================

Architecture BiLSTM
-------------------

.. code-block:: python

   from tensorflow.keras.models import Sequential
   from tensorflow.keras.layers import Bidirectional, LSTM, Dense
   
   model = Sequential()
   model.add(Bidirectional(LSTM(64, return_sequences=True), 
             input_shape=(seq_length, 4)))
   model.add(Bidirectional(LSTM(32)))
   model.add(Dense(32, activation='relu'))
   model.add(Dense(2))  # lat + lon

Hyperparamètres optimaux
------------------------
* Optimiseur: **Adam**
* Taille de lot: **8**
* Longueur séquence: **5**
* Fonction de perte: Distance euclidienne

Performances
------------
* MAE: 4.2693
* MSE: 41.3673
* Temps d'entraînement: 5 min/époque
