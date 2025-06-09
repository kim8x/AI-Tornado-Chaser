API
===

Overview
--------
The API component allows you to serve predictions from your trained models using Flask. This makes it possible to integrate your tornado forecasting models into other applications or services.

How it Works
------------
- The API loads your trained model and scaler.
- It exposes a REST endpoint (e.g., `/predict`) that accepts POST requests with input data.
- The API returns predictions as a JSON response.

Example Usage
-------------
1. Start the API by running the code in `API.ipynb` or by exporting it to a Python script and running it:
   ```powershell
   python model_api.py
   ```
2. Send a POST request to the `/predict` endpoint with your input data in JSON format.
3. Receive the predicted sequence in the response.

API Endpoint
------------
- **POST /predict**
  - Input: JSON object with time series data
  - Output: JSON object with predicted sequence

See the `API.ipynb` notebook for implementation details and examples.
