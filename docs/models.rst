Models
======

Model Overview
-------------
The project implements several deep learning and machine learning models for tornado prediction:

LSTM Models
----------
- Bidirectional LSTM (BiLSTM)
- Standard LSTM
- Multi-layer LSTM

Traditional Models
----------------
- XGBoost Regression
- Simple RNN
- MLP (Multi-Layer Perceptron)

Model Training
-------------
All models are trained using historical tornado data with the following features:
- Latitude and Longitude
- Intensity
- Pressure
- Wind Speed
- Additional meteorological parameters

Model Comparison
---------------
Models are evaluated using:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Custom evaluation metrics for tornado prediction

Best Practices
-------------
- Use normalized/scaled data
- Maintain consistent sequence lengths
- Save model checkpoints
- Document hyperparameters
