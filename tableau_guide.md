# Tableau Dashboard - Step by Step

## Step 1: Data Connect
Tableau Public kholo > Connect > Text File > clean_data.csv

## Step 2: Calculated Fields
Avg U: AVG([U])
Total Saving: SUM([saving_usd])
Fouling Alert: IF [fouling_pct] > 5 THEN 'CLEANING REQUIRED' ELSE 'HEALTHY' END
Efficiency Category: IF [U] > 1500 THEN 'Excellent' ELSEIF [U] > 1000 THEN 'Good' ELSE 'Poor' END
Monthly Saving: {FIXED [Month] : SUM([saving_usd])}

## Step 3: Sheets Banao
Sheet 1: Line - Month vs Avg U
Sheet 2: Bar - Month vs Saving
Sheet 3: Scatter - m_hot vs U
Sheet 4: Map / Heatmap - Fouling %
Sheet 5: KPI Dashboard - Combine all

## Step 4: Dashboard
Dashboard > Show Title > Add Filters > Publish to Tableau Public > Link Resume ch