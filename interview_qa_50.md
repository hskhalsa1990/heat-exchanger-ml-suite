# Interview Q&A - 50 Questions - Heat Exchanger + Data Science

## Python / Pandas (1-10)
Q1. Pandas ch missing value kive handle karde? A: dropna(), fillna(mean/median)
Q2. Duplicate kive remove? A: drop_duplicates()
Q3. Outlier kive? A: IQR method, Z-score, U>5000 filter
Q4. GroupBy kive kam karda? A: Monthly saving layi groupby Month
Q5. Merge vs Join? A: Merge on column, Join on index
Q6. List vs Tuple? A: List mutable, Tuple immutable
Q7. Lambda function? A: Small anonymous function
Q8. Pandas vs NumPy? A: Pandas tabular, NumPy numerical
Q9. read_csv ch chunksize kyu? A: Large file layi
Q10. Feature Engineering ki kitta? A: LMTD, Q, Efficiency banaye

## Machine Learning (11-20)
Q11. Random Forest kive kam karda? A: Many trees, voting
Q12. XGBoost kyu best? A: Gradient boosting, tabular data te best
Q13. Overfitting ki hai? A: Train te changa, Test te mada - Solution: Cross-validation
Q14. R2 Score ki hai? A: 0-1, 0.96 matlab 96% variance explain
Q15. Train-Test Split kyu? A: Model nu unseen data te test karan layi
Q16. StandardScaler kyu? A: ANN layi features same scale te
Q17. Hyperparameter tuning? A: GridSearchCV / Optuna
Q18. Bias vs Variance? A: Bias underfit, Variance overfit
Q19. Regression vs Classification? A: Regression continuous (U), Classification category (Healthy/Fouling)
Q20. Feature Importance? A: m_hot sab to important hai

## Deep Learning (21-30)
Q21. ANN ki hai? A: Input-Hidden-Output layers
Q22. Activation function? A: ReLU, Sigmoid
Q23. LSTM kyu? A: Time-series fouling prediction layi - past U to future U
Q24. PINN ki hai? A: Physics loss + Data loss, Q - U*A*LMTD = 0
Q25. CNN ki hai? A: Image layi - Thermal image fouling detection
Q26. Epoch vs Batch? A: Epoch full data ek vaar, Batch small part
Q27. Loss function? A: MSE for regression
Q28. Optimizer? A: Adam
Q29. Dropout kyu? A: Overfitting rokhan layi
Q30. Transfer Learning? A: Pretrained model use karna

## Computer Vision (31-35)
Q31. CV ch ki kitta? A: Thermal image to hot spot detect
Q32. OpenCV thresholding? A: Temp > 85 = Fouling pixel
Q33. YOLO kyu? A: Real-time object detection - Hot spot
Q34. CNN vs YOLO? A: CNN classification, YOLO detection + location
Q35. Image augmentation? A: Rotate, flip data vadhaun layi

## SQL (36-40)
Q36. SELECT vs WHERE? A: SELECT columns, WHERE filter
Q37. GROUP BY kive? A: Monthly saving layi
Q38. JOIN types? A: INNER, LEFT, RIGHT, FULL
Q39. Window Function? A: Running total saving - SUM() OVER()
Q40. View ki hai? A: Saved query - vw_dashboard

## Power BI / Tableau / Excel (41-47)
Q41. DAX ki hai? A: Power BI formula language - SUM, AVERAGE, CALCULATE
Q42. Power BI vs Tableau? A: Power BI Microsoft, Tableau visualisation strong
Q43. Calculated Field Tableau ch? A: IF fouling>5 THEN Cleaning
Q44. Excel Dashboard ch ki? A: 3 Sheets - Raw, Monthly, KPI
Q45. Slicer kyu? A: Filter layi - Month, Status
Q46. Power BI Publish kive? A: File > Publish > Service
Q47. KPI ki ne? A: Avg U, Total Saving, Fouling Alerts

## Project / HR (48-50)
Q48. Sales bina sell record to kive? A: Energy Saving * Rate = Revenue, No fake sales
Q49. Industrial use? A: Refinery, Chemical Plant, Pharma - 24x7 monitoring
Q50. Future Scope? A: IoT Sensors + Real-time API + Auto Cleaning Alert