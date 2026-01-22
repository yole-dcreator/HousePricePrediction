#!/usr/bin/env python3
"""
Verification Script for House Price Prediction System
Run this script to verify all components are working correctly
"""

import os
import sys
import json

def check_file_exists(path, description):
    """Check if a file or directory exists"""
    if os.path.exists(path):
        print(f"✓ {description}: {path}")
        return True
    else:
        print(f"✗ {description}: {path} - NOT FOUND")
        return False

def check_directory_exists(path, description):
    """Check if a directory exists and list its contents"""
    if os.path.isdir(path):
        files = os.listdir(path)
        print(f"✓ {description}: {path}")
        for f in files:
            print(f"  └─ {f}")
        return True
    else:
        print(f"✗ {description}: {path} - NOT FOUND")
        return False

def main():
    print("=" * 60)
    print("HOUSE PRICE PREDICTION SYSTEM - VERIFICATION SCRIPT")
    print("=" * 60)
    print()
    
    # Get current directory
    base_dir = os.getcwd()
    print(f"Verifying project at: {base_dir}")
    print()
    
    # Check project structure
    print("1. CHECKING PROJECT STRUCTURE")
    print("-" * 60)
    
    checks = [
        ("model_building.ipynb", "Model Development Notebook"),
        ("app.py", "Flask Application"),
        ("requirements.txt", "Requirements File"),
        ("README.md", "README Documentation"),
        ("DEPLOYMENT_GUIDE.md", "Deployment Guide"),
        ("HousePrice_hosted_webGUI_link.txt", "Submission Template"),
        ("PROJECT_COMPLETION_SUMMARY.md", "Project Summary"),
        (".gitignore", "Git Ignore File"),
    ]
    
    files_ok = True
    for file, desc in checks:
        if not check_file_exists(file, desc):
            files_ok = False
    print()
    
    # Check directories
    print("2. CHECKING DIRECTORIES")
    print("-" * 60)
    
    dirs_ok = True
    dirs = [
        ("model", "Model Directory"),
        ("templates", "Templates Directory"),
        ("static", "Static Directory"),
    ]
    
    for dir_name, desc in dirs:
        if not check_directory_exists(dir_name, desc):
            dirs_ok = False
    print()
    
    # Check model files
    print("3. CHECKING MODEL FILES")
    print("-" * 60)
    
    model_files = [
        ("model/house_prices_train.csv", "Dataset"),
        ("model/house_price_model.pkl", "Trained Model"),
        ("model/scaler.pkl", "Feature Scaler"),
        ("model/label_encoders.pkl", "Label Encoders"),
        ("model/model_config.json", "Model Configuration"),
    ]
    
    model_ok = True
    for file, desc in model_files:
        if not check_file_exists(file, desc):
            model_ok = False
    print()
    
    # Check template files
    print("4. CHECKING TEMPLATE FILES")
    print("-" * 60)
    
    template_files = [
        ("templates/index.html", "Main HTML Template"),
        ("static/style.css", "CSS Stylesheet"),
    ]
    
    template_ok = True
    for file, desc in template_files:
        if not check_file_exists(file, desc):
            template_ok = False
    print()
    
    # Try to import and test components
    print("5. TESTING COMPONENT IMPORTS")
    print("-" * 60)
    
    import_ok = True
    
    try:
        import flask
        print("✓ Flask imported successfully")
    except ImportError:
        print("✗ Flask not found - please run: pip install -r requirements.txt")
        import_ok = False
    
    try:
        import pandas
        print("✓ Pandas imported successfully")
    except ImportError:
        print("✗ Pandas not found")
        import_ok = False
    
    try:
        import numpy
        print("✓ NumPy imported successfully")
    except ImportError:
        print("✗ NumPy not found")
        import_ok = False
    
    try:
        import sklearn
        print("✓ scikit-learn imported successfully")
    except ImportError:
        print("✗ scikit-learn not found")
        import_ok = False
    
    try:
        import joblib
        print("✓ Joblib imported successfully")
    except ImportError:
        print("✗ Joblib not found")
        import_ok = False
    print()
    
    # Try to load model
    print("6. TESTING MODEL LOADING")
    print("-" * 60)
    
    model_load_ok = False
    try:
        import joblib
        model = joblib.load('model/house_price_model.pkl')
        print("✓ Model loaded successfully")
        scaler = joblib.load('model/scaler.pkl')
        print("✓ Scaler loaded successfully")
        encoders = joblib.load('model/label_encoders.pkl')
        print("✓ Label encoders loaded successfully")
        
        with open('model/model_config.json', 'r') as f:
            config = json.load(f)
        print("✓ Model configuration loaded successfully")
        print(f"  - Algorithm: {config['model_algorithm']}")
        print(f"  - Features: {', '.join(config['selected_features'])}")
        print(f"  - Test R²: {config['model_metrics']['test_r2']:.4f}")
        
        model_load_ok = True
    except Exception as e:
        print(f"✗ Error loading model: {e}")
    print()
    
    # Summary
    print("=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    
    all_ok = files_ok and dirs_ok and model_ok and template_ok and import_ok and model_load_ok
    
    print(f"Project Structure:    {'✓ OK' if files_ok and dirs_ok else '✗ ISSUES FOUND'}")
    print(f"Model Files:          {'✓ OK' if model_ok else '✗ ISSUES FOUND'}")
    print(f"Template Files:       {'✓ OK' if template_ok else '✗ ISSUES FOUND'}")
    print(f"Dependencies:         {'✓ OK' if import_ok else '✗ ISSUES FOUND'}")
    print(f"Model Loading:        {'✓ OK' if model_load_ok else '✗ ISSUES FOUND'}")
    print()
    
    if all_ok:
        print("✓ ALL CHECKS PASSED! System is ready for deployment.")
        print()
        print("Next steps:")
        print("1. Run locally: python app.py")
        print("2. Open: http://localhost:5000")
        print("3. Test the prediction form")
        print("4. Deploy using DEPLOYMENT_GUIDE.md")
        print("5. Update HousePrice_hosted_webGUI_link.txt with live URL")
        print("6. Submit to Scorac")
        return 0
    else:
        print("✗ SOME CHECKS FAILED. Please fix the issues above.")
        print()
        if not import_ok:
            print("To fix dependency issues, run:")
            print("  pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())
