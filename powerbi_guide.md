# Power BI Dashboard - Step by Step

## Step 1: Data Import
Power BI Desktop kholo > Get Data > CSV > clean_data.csv select karo

## Step 2: DAX Formulas - Copy Paste Karo
Avg_U = AVERAGE(exchanger_data[U])
Total_Saving = SUM(exchanger_data[saving_usd])
Total_Q = SUM(exchanger_data[Q])
Fouling_Alert_Count = COUNTROWS(FILTER(exchanger_data, exchanger_data[fouling_pct] > 5))
Healthy_Pct = DIVIDE(COUNTROWS(FILTER(exchanger_data, exchanger_data[fouling_pct] <= 5)), COUNTROWS(exchanger_data)) * 100
Monthly_Saving = CALCULATE(SUM(exchanger_data[saving_usd]), DATESMTD(exchanger_data[Date]))

## Step 3: Visuals Banao
1. KPI Cards: Avg U, Total Saving, Fouling Alerts
2. Line Chart: Month vs Avg U - Fouling trend dikhega
3. Bar Chart: Month vs Saving - Sales jiveh
4. Gauge Chart: Fouling % - 5% to upar ta Red
5. Scatter: m_hot vs U (Color = Q)
6. Slicer: Status, Month, Area

## Step 4: Publish
File > Publish > Power BI Service > Share Link Resume ch pao