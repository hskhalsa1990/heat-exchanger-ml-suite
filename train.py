"""Train a Random Forest to predict overall heat transfer coefficient U."""
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

FEATURES = ['Th_in', 'Tc_in', 'm_hot', 'm_cold', 'Area', 'k_material', 'flow_type']

if __name__ == '__main__':
    df = pd.read_csv('data_ml_heat_exchanger.csv')
    X_tr, X_te, y_tr, y_te = train_test_split(df[FEATURES], df['U'], test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=200, random_state=42).fit(X_tr, y_tr)
    print(f'R2 on test set: {r2_score(y_te, model.predict(X_te)):.3f}')
    joblib.dump(model, 'model.joblib')
