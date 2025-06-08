Évaluation comparative
======================

Comparaison des optimiseurs
---------------------------

.. list-table::
   :header-rows: 1
   
   * - Optimiseur
     - MAE
     - MSE
   * - **Adam**
     - **4.2693**
     - **41.3673**
   * - RMSprop
     - 9.0301
     - 154.0797
   * - Adagrad
     - 25.8452
     - 1275.2479

Comparaison des architectures
-----------------------------

.. list-table::
   :header-rows: 1
   
   * - Modèle
     - Performance
   * - **BiLSTM**
     - **1ère**
   * - LSTM
     - 2ème
   * - GRU
     - 3ème
   * - MLP
     - 6ème

Analyse des courbes d'apprentissage
-----------------------------------
1. Phase initiale (0-20 époques): Apprentissage rapide
2. Phase de stabilisation (20-150 époques): Améliorations marginales
3. Point optimal: ~50 époques