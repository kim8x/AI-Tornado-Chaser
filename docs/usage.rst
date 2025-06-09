Usage
=====

Setup Instructions
------------------
1. Install Python 3.8 or higher.
2. Install dependencies:
   - Open a terminal in the project directory.
   - Run: ``pip install -r docs/requirements.txt``
3. (Optional) If using Google Colab, mount your Google Drive and adjust file paths as needed.
4. Open the notebooks in Jupyter or VS Code.

How to Use
----------
- Start with ``final_times_series_project.ipynb`` to explore the data, preprocess, and train models.
- Use ``time_series_model_1.ipynb`` for additional analysis and feature engineering.
- After training, use ``API.ipynb`` as a template to deploy your model for predictions via a REST API.
- Adjust parameters, experiment with different models, and compare results.

Best Practices
--------------
- Always normalize or scale your input data using the same scaler as during training.
- Save your trained models and scalers for reproducibility.
- Evaluate multiple models to select the best performer.
- Document your experiments and results in the notebooks.
