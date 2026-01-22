# House Price Prediction System

A machine learning-based house price prediction system built with Flask and Random Forest Regressor.

## Project Overview

This project implements a complete house price prediction system using:
- **Machine Learning Algorithm**: Random Forest Regressor
- **Selected Features** (6 of 9 recommended):
  - Overall Quality (OverallQual)
  - Ground Living Area (GrLivArea)
  - Total Basement Area (TotalBsmtSF)
  - Garage Cars (GarageCars)
  - Year Built (YearBuilt)
  - Neighborhood

## Model Performance

- **Test R² Score**: 0.8861
- **Test RMSE**: $29,558.89
- **Test MAE**: $18,688.95

## Project Structure

```
HousePrice_Project/
├── app.py                    # Flask web application
├── model_building.ipynb      # Model development notebook
├── requirements.txt          # Python dependencies
├── model/
│   ├── house_prices_train.csv    # Original dataset
│   ├── house_price_model.pkl     # Trained model
│   ├── scaler.pkl                # Feature scaler
│   ├── label_encoders.pkl        # Categorical encoders
│   └── model_config.json         # Model configuration
├── static/
│   └── style.css            # CSS styling
└── templates/
    └── index.html           # HTML template
```

## Installation

1. Clone the repository or download the project files
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Using the Web GUI

1. Navigate to the web application in your browser
2. Enter house details:
   - Overall Quality (1-10)
   - Ground Living Area (sq ft)
   - Total Basement Area (sq ft)
   - Garage Cars (0-5)
   - Year Built (1800-2025)
   - Select Neighborhood
3. Click "Predict Price"
4. View the predicted house price

### API Endpoint

You can also use the REST API endpoint:

**Endpoint**: `POST /api/predict`

**Request Body**:
```json
{
  "OverallQual": 7,
  "GrLivArea": 1710,
  "TotalBsmtSF": 856,
  "GarageCars": 2,
  "YearBuilt": 2003,
  "Neighborhood": "CollgCr"
}
```

**Response**:
```json
{
  "success": true,
  "predicted_price": 235000.45,
  "features": {
    "OverallQual": 7,
    "GrLivArea": 1710,
    "TotalBsmtSF": 856,
    "GarageCars": 2,
    "YearBuilt": 2003,
    "Neighborhood": "CollgCr"
  }
}
```

## Model Development

The model was developed using the following steps:

1. **Data Loading & Exploration**: Analyzed the house prices dataset
2. **Data Preprocessing**: Handled missing values, removed outliers
3. **Feature Selection**: Selected 6 of 9 recommended features
4. **Feature Encoding**: Label-encoded categorical features (Neighborhood)
5. **Feature Scaling**: Applied StandardScaler for normalization
6. **Train-Test Split**: 80-20 split for evaluation
7. **Model Training**: Random Forest Regressor with 100 trees
8. **Model Evaluation**: Evaluated using MAE, MSE, RMSE, and R²
9. **Model Persistence**: Saved using joblib

## Technologies Used

- **Python 3.8+**
- **Flask 2.3+** - Web framework
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **joblib** - Model persistence
- **HTML/CSS** - Frontend

## Deployment

The application can be deployed on:
- Render.com
- PythonAnywhere.com
- Streamlit Cloud
- Vercel (with backend configuration)

## Notes

- The model is trained on historical house price data
- Predictions are based on 6 selected features
- Input values are validated before prediction
- The model predicts prices in USD

## Author

Created as part of a machine learning project assignment.

## License

This project is provided as-is for educational purposes.
