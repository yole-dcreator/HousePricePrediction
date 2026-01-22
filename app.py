"""
House Price Prediction Web Application
Built with Flask
"""

from flask import Flask, render_template, request, jsonify
import joblib
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

# Initialize Flask app
app = Flask(__name__)

# Load model and preprocessing objects
MODEL_PATH = 'model/house_price_model.pkl'
SCALER_PATH = 'model/scaler.pkl'
ENCODERS_PATH = 'model/label_encoders.pkl'
CONFIG_PATH = 'model/model_config.json'

# Load the trained model
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
label_encoders = joblib.load(ENCODERS_PATH)

# Load model configuration
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

SELECTED_FEATURES = config['selected_features']
NEIGHBORHOODS = [
    'Blmngtn', 'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr',
    'Crawfor', 'Edwards', 'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel',
    'Names', 'NoRidge', 'NPkVill', 'NridgHt', 'NWAmes', 'OldTown',
    'SWISU', 'Sawyer', 'SawyerW', 'Somerst', 'StoneBr', 'Timber',
    'Veenker'
]


@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html', neighborhoods=NEIGHBORHOODS)


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    API endpoint for house price prediction
    Expects JSON data with house features
    """
    try:
        # Get data from request
        data = request.get_json()

        # Extract features
        features_dict = {
            'OverallQual': float(data.get('OverallQual', 5)),
            'GrLivArea': float(data.get('GrLivArea', 1500)),
            'TotalBsmtSF': float(data.get('TotalBsmtSF', 1000)),
            'GarageCars': float(data.get('GarageCars', 2)),
            'YearBuilt': float(data.get('YearBuilt', 2000)),
            'Neighborhood': str(data.get('Neighborhood', 'CollgCr'))
        }

        # Validate input ranges
        if not (1 <= features_dict['OverallQual'] <= 10):
            return jsonify({'error': 'OverallQual must be between 1 and 10'}), 400

        if features_dict['GrLivArea'] <= 0:
            return jsonify({'error': 'GrLivArea must be positive'}), 400

        if features_dict['TotalBsmtSF'] < 0:
            return jsonify({'error': 'TotalBsmtSF must be non-negative'}), 400

        if not (0 <= features_dict['GarageCars'] <= 5):
            return jsonify({'error': 'GarageCars must be between 0 and 5'}), 400

        if not (1800 <= features_dict['YearBuilt'] <= 2025):
            return jsonify({'error': 'YearBuilt must be between 1800 and 2025'}), 400

        if features_dict['Neighborhood'] not in NEIGHBORHOODS:
            return jsonify({'error': f"Neighborhood must be one of: {', '.join(NEIGHBORHOODS)}"}), 400

        # Create feature array
        feature_values = []
        for feature_name in SELECTED_FEATURES:
            if feature_name == 'Neighborhood':
                # Encode categorical feature
                encoded_value = label_encoders['Neighborhood'].transform([features_dict['Neighborhood']])[0]
                feature_values.append(encoded_value)
            else:
                feature_values.append(features_dict[feature_name])

        # Convert to numpy array and reshape
        features_array = np.array(feature_values).reshape(1, -1)

        # Scale features
        features_scaled = scaler.transform(features_array)

        # Make prediction
        predicted_price = model.predict(features_scaled)[0]

        # Ensure price is positive
        predicted_price = max(0, predicted_price)

        return jsonify({
            'success': True,
            'predicted_price': round(predicted_price, 2),
            'features': features_dict
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/model-info', methods=['GET'])
def model_info():
    """Get model information"""
    return jsonify({
        'algorithm': config['model_algorithm'],
        'features': SELECTED_FEATURES,
        'metrics': config['model_metrics'],
        'neighborhoods': NEIGHBORHOODS
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'model': 'loaded'})


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
