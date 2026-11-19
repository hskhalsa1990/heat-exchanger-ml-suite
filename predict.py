"""Predict U with the trained model. Run train.py first."""
import joblib
import pandas as pd
from train import FEATURES

if __name__ == '__main__':
    model = joblib.load('model.joblib')
    sample = pd.DataFrame([[90, 25, 1.2, 1.2, 3.0, 200, 1]], columns=FEATURES)
    print(f'Predicted U: {model.predict(sample)[0]:.1f} W/m2K')
