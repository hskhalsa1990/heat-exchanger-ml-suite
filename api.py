"""FastAPI service. Run: uvicorn api:app --reload"""
from fastapi import FastAPI

app = FastAPI(title='Heat Exchanger API')


@app.get('/')
def home():
    return {'status': 'Running', 'plant': 'Ludhiana Refinery Unit-2'}


@app.get('/health')
def health():
    return {'healthy': True}


@app.post('/predict')
def predict(Th_in: float, Tc_in: float, m_hot: float, Area: float):
    U = 800 + 400 * m_hot + 100 * Area
    Q = U * Area * 30
    saving = (U - 900) * Area * 30 * 8000 * 0.12 / 1000
    return {'U': U, 'Q': Q, 'fouling_alert': U < 800, 'saving_usd_per_year': saving}
