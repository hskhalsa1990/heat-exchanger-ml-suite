# 🔥 Heat Exchanger ML Suite

End-to-end heat exchanger project: **physics + machine learning + fouling prediction + dashboards + API + SQL/BI + fin heat-transfer analysis**, all in one flat repository (no sub-folders).

> Merged from: `heat-exchanger-ml-project`, `-INDUSTRIAL`, `-DATA-SCIENCE-PRO`, `-MEGA-PACK`, `-SYLLABUS-PRO` and the Fin Heat Transfer Colab project.

---

## 🗺️ Architecture

```mermaid
flowchart LR
    A[Sensors / CSV data] --> B[Data cleaning<br/>pandas]
    B --> C[Physics layer<br/>physics.py, kern_method.py]
    B --> D[ML models<br/>train.py]
    C --> E[PINN loss<br/>pinn_model.py]
    D --> F[Predictions<br/>predict.py]
    E --> F
    F --> G[FastAPI<br/>api.py]
    F --> H[Streamlit<br/>dashboard.py]
    F --> I[Power BI / Tableau / Excel]
    G --> J[Docker]
    H --> K[Fouling alert + cost saving]
```

## 🔬 Heat exchanger physics

```mermaid
flowchart TD
    Q[Heat duty Q = U x A x LMTD] --> U[U: overall coefficient]
    Q --> LM[LMTD from terminal temperatures]
    U --> F[Fouling Rf = 1/U_fouled - 1/U_clean]
    F --> CL{Fouling > 5%?}
    CL -- Yes --> ALERT[Cleaning alert]
    CL -- No --> OK[Healthy]
    ALERT --> COST[Cost model: capital + pumping<br/>cost.py]
```

## 🤖 ML / data pipeline

```mermaid
flowchart LR
    RAW[data_science_raw_dirty.csv] -->|clean| CLEAN[data_science_clean.csv]
    CLEAN --> FE[Feature engineering<br/>LMTD, Q, efficiency]
    FE --> SPLIT[Train / test split]
    SPLIT --> RF[Random Forest]
    SPLIT --> XGB[XGBoost]
    SPLIT --> ANN[ANN / LSTM / PINN]
    RF --> EVAL[R2 score]
    XGB --> EVAL
    ANN --> EVAL
    EVAL --> DEP[API + Dashboard]
```

## 🧩 Fin heat-transfer notebook flow

```mermaid
flowchart LR
    P[Fin geometry + material<br/>L, t, w, k, h] --> T[Temperature profile<br/>cosh solution]
    T --> EFF[Fin efficiency<br/>tanh mL / mL]
    EFF --> G2[7 x 2D graphs]
    EFF --> G3[4 x 3D graphs]
    EFF --> TB[2 comparison tables]
    EFF --> ML[Random Forest efficiency model]
```

---

## 📁 File map (flat layout)

| Group | Files |
| :--- | :--- |
| Physics and design | `physics.py`, `kern_method.py`, `cost.py`, `pinn_model.py` |
| ML | `train.py`, `predict.py`, `notebook_heat_exchanger_ml.ipynb` |
| Fin analysis | `notebook_fin_heat_transfer_colab.ipynb` |
| Serving | `api.py` (FastAPI), `flask_app.py`, `dashboard.py` (Streamlit), `Dockerfile` |
| Data | `data_ml_heat_exchanger.csv`, `data_industrial_fouling.csv`, `data_monitoring_clean.csv`, `data_syllabus_clean.csv`, `data_science_clean.csv`, `data_science_raw_dirty.csv` |
| Stats | `stats_report.txt`, `stats_descriptive.csv` |
| SQL / NoSQL | `sql_database.sql` (15 queries), `mongodb_queries.js` |
| BI | `Excel_Dashboard.xlsx`, `powerbi_guide.md`, `dax_formulas.txt`, `tableau_guide.md` |
| MLOps | `etl_pipeline.py`, `deploy_aws_gcp_azure.md` |
| Interview / business | `interview_qa_50.md`, `interview_qa_syllabus.md`, `storytelling_business.md` |
| Tests | `test_physics.py` |
| Images | `img_*.png` |

## 🚀 Quick start

```bash
pip install -r requirements.txt

python train.py                 # trains Random Forest, saves model.joblib
python predict.py               # sample prediction of U
streamlit run dashboard.py      # live dashboard
uvicorn api:app --reload        # REST API (docs at /docs)
pytest                          # run tests
docker build -t hx-suite . && docker run -p 8000:8000 hx-suite
```

Fin analysis: upload `notebook_fin_heat_transfer_colab.ipynb` to Google Colab and use Runtime > Run all.

## 📐 Physics used

- Conduction: `Q = k·A·dT/dx`
- Convection: `Q = h·A·(Ts − Tf)`
- Radiation: `Q = ε·σ·A·(Ts⁴ − Tsurr⁴)`
- Heat exchanger: `Q = U·A·LMTD`
- Fouling resistance: `Rf = 1/U_fouled − 1/U_clean`
- PINN loss: `MSE_data + λ·MSE_physics`, physics term `Q − U·A·LMTD = 0`

## 🖼️ Diagrams

| | |
| :---: | :---: |
| ![2D temperature profile](img_ml_2d_temperature_profile.png) | ![3D U surface](img_ml_3d_U_surface.png) |
| ![3D Q scatter](img_ml_3d_Q_scatter.png) | ![Model comparison](img_ml_model_comparison.png) |
| ![3D fouling prediction](img_industrial_3d_fouling.png) | ![Cost optimization](img_industrial_cost_optimization.png) |
| ![2D visualisation](img_ds_visualisation_2d.png) | ![3D visualisation](img_ds_visualisation_3d.png) |
| ![Thermal image](img_ds_thermal_image.png) | ![Sales / saving](img_ds_sales_saving.png) |
| ![EDA](img_syllabus_eda.png) | |

## ⚠️ Notes

- Data is synthetic and for learning / portfolio use, not real plant data.
- `api.py` and `dashboard.py` use a simplified U formula for demo; real design uses `kern_method.py` / the trained model.
- Run `python train.py` to see the actual R² on your machine.

## 📜 License

MIT
