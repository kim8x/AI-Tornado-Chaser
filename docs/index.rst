AI Tornado Chaser Documentation
==============================

.. toctree::
   :maxdepth: 2
   :caption: Contents

   introduction
   usage
   api
   contributing

Introduction
------------
AI Tornado Chaser is a machine learning project focused on analyzing and forecasting tornado events using time series data. It provides Jupyter Notebooks for data exploration, model development, and an API for making predictions.

Features
--------
- Data loading, cleaning, and preprocessing
- Exploratory data analysis and visualization
- Model training and evaluation (LSTM, BiLSTM, XGBoost, and more)
- Model selection and comparison
- API for serving predictions using Flask

Project Structure
-----------------
- ``final_times_series_project.ipynb``: Main notebook for data processing, model selection, and evaluation. Includes:
  - Data import and normalization
  - Sequence creation for time series
  - Model training (LSTM, BiLSTM, MLP, etc.)
  - Model evaluation and comparison
  - Saving scalers and models for later use
- ``API.ipynb``: Example Flask API to serve model predictions. Includes:
  - Loading trained models and scalers
  - REST endpoint for predictions
  - Example usage for integrating with other applications
- ``time_series_model_1.ipynb``: Additional data analysis and modeling. Includes:
  - Data exploration and visualization
  - Feature engineering
  - XGBoost regression modeling
- ``README.md``: Quick reference and project summary

Setup Instructions
------------------
1. Install Python 3.8 or higher.
2. Install dependencies:
   - Open a terminal in the project directory.
   - Run: ``pip install -r docs/requirements.txt``
3. (Optional) If using Google Colab, mount your Google Drive and adjust file paths as needed.
4. Open the notebooks in Jupyter or VS Code.

Usage Guide
-----------
- Start with ``final_times_series_project.ipynb`` to explore the data, preprocess, and train models.
- Use ``time_series_model_1.ipynb`` for additional analysis and feature engineering.
- After training, use ``API.ipynb`` as a template to deploy your model for predictions via a REST API.
- Adjust parameters, experiment with different models, and compare results.

API Overview
------------
- The API notebook demonstrates how to serve predictions from a trained model using Flask.
- Example endpoint: ``/predict`` (POST)
- Input: JSON with time series data
- Output: JSON with predicted sequence
- To run the API: execute the notebook or export the code to a Python script and run it with Python.

Best Practices
--------------
- Always normalize or scale your input data using the same scaler as during training.
- Save your trained models and scalers for reproducibility.
- Evaluate multiple models to select the best performer.
- Document your experiments and results in the notebooks.

Contributing
------------
- Fork the repository and create a new branch for your feature or bugfix.
- Submit a pull request with a clear description of your changes.
- For questions or support, refer to the ``README.md`` or open an issue in your repository platform.

Contact
-------
For further information, please refer to the ``README.md`` or contact the project maintainer via the repository platform.