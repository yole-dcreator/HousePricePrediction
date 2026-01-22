# DEPLOYMENT GUIDE FOR HOUSE PRICE PREDICTION SYSTEM

## Quick Start

This guide will help you deploy the House Price Prediction System to a cloud platform.

---

## OPTION 1: Deploy on Render.com (Recommended)

### Step 1: Prepare Your Repository

1. Initialize a Git repository (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: House Price Prediction System"
   ```

2. Create a GitHub repository and push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/HousePrice_Project_YourMatricNo.git
   git push -u origin main
   ```

### Step 2: Create Render Account

1. Go to https://render.com
2. Sign up with your GitHub account
3. Connect your GitHub account

### Step 3: Deploy on Render

1. Click "Create" → "Web Service"
2. Connect your GitHub repository
3. Fill in the following details:
   - **Name**: `house-price-prediction`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Add these variables:
     - `FLASK_ENV=production`

4. Click "Create Web Service"
5. Wait for deployment to complete (3-5 minutes)
6. Your app will be available at: `https://house-price-prediction.onrender.com`

### Important: Install Gunicorn

Add `gunicorn==21.2.0` to requirements.txt for production deployment:

```
Flask==2.3.2
gunicorn==21.2.0
numpy==1.24.3
pandas==2.0.2
scikit-learn==1.2.2
joblib==1.2.0
matplotlib==3.7.1
seaborn==0.12.2
Werkzeug==2.3.6
```

---

## OPTION 2: Deploy on PythonAnywhere.com

### Step 1: Create Account

1. Go to https://www.pythonanywhere.com
2. Sign up for a free account

### Step 2: Upload Files

1. Go to "Files" section
2. Upload your project files
3. Or use bash console to clone from GitHub:
   ```bash
   git clone https://github.com/YOUR_USERNAME/HousePrice_Project_YourMatricNo.git
   ```

### Step 3: Create Web App

1. Click "Web" → "Add a new web app"
2. Choose "Manual configuration"
3. Select Python 3.8+
4. Configure WSGI file to point to your Flask app

### Step 4: Configure

1. Set up virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.8 myapp
   pip install -r requirements.txt
   ```

2. Update WSGI configuration file with:
   ```python
   import sys
   sys.path.insert(0, '/home/USERNAME/HousePrice_Project_YourMatricNo')
   from app import app as application
   ```

3. Your app will be available at: `https://USERNAME.pythonanywhere.com`

---

## OPTION 3: Deploy on Streamlit Cloud

### Step 1: Modify App for Streamlit

Create a new file `streamlit_app.py`:
```python
import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load model and preprocessing
model = joblib.load('model/house_price_model.pkl')
scaler = joblib.load('model/scaler.pkl')
label_encoders = joblib.load('model/label_encoders.pkl')

st.title('🏠 House Price Prediction System')

# Input fields
col1, col2 = st.columns(2)
with col1:
    overall_qual = st.slider('Overall Quality', 1, 10, 5)
    gr_liv_area = st.number_input('Ground Living Area (sq ft)', 300, 5000, 1500)
    total_bsmt_sf = st.number_input('Total Basement Area (sq ft)', 0, 6000, 1000)

with col2:
    garage_cars = st.number_input('Garage Cars', 0, 5, 2)
    year_built = st.number_input('Year Built', 1800, 2025, 2000)
    neighborhood = st.selectbox('Neighborhood', NEIGHBORHOODS)

if st.button('Predict Price'):
    # Prepare features
    features = [overall_qual, gr_liv_area, total_bsmt_sf, garage_cars, year_built]
    features.append(label_encoders['Neighborhood'].transform([neighborhood])[0])
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)[0]
    
    st.success(f'Predicted Price: ${prediction:,.2f}')
```

### Step 2: Deploy

1. Push to GitHub with `streamlit_app.py`
2. Go to https://share.streamlit.io
3. Click "Deploy an app"
4. Select your repository and `streamlit_app.py`
5. App will be live in minutes!

---

## OPTION 4: Local Development & Testing

### Before Deployment

1. Install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run locally:
   ```bash
   python app.py
   ```

3. Test the application:
   ```bash
   curl http://localhost:5000/health
   ```

4. Open browser to: `http://localhost:5000`

---

## Troubleshooting

### Issue: Model not found during deployment
- Ensure `model/house_price_model.pkl` is in repository
- Check relative paths in `app.py`

### Issue: Dependencies not installing
- Check Python version compatibility (Python 3.8+)
- Ensure all packages in requirements.txt are available

### Issue: Port conflicts
- Change port in `app.py` from 5000 to another available port
- On Render/PythonAnywhere, port is automatically assigned

### Issue: High memory usage
- Model size is optimized, but if needed, use model quantization
- Consider using a micro instance tier

---

## After Deployment

1. Test all features on live URL
2. Update `HousePrice_hosted_webGUI_link.txt` with your live URL
3. Commit and push updates to GitHub
4. Submit to Scorac with all required information

---

## Support

For deployment issues:
- Render support: https://render.com/docs
- PythonAnywhere help: https://www.pythonanywhere.com/help/
- Streamlit docs: https://docs.streamlit.io

---

**Deployment Deadline: Friday, January 22, 2026, 11:59 PM**

Good luck with your deployment! 🚀
