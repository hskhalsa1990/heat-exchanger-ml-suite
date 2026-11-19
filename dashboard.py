"""Streamlit dashboard. Run: streamlit run dashboard.py"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Heat Exchanger Dashboard', layout='wide')
st.title('Heat Exchanger - Live Industrial Dashboard')

st.sidebar.header('Operating Parameters')
Th_in = st.sidebar.slider('Hot Inlet Temp (C)', 60, 120, 90)
Tc_in = st.sidebar.slider('Cold Inlet Temp (C)', 10, 40, 25)
m_hot = st.sidebar.slider('Hot Flow (kg/s)', 0.5, 3.0, 1.2)
Area = st.sidebar.slider('Area (m2)', 1.0, 10.0, 3.0)

U = 800 + 400 * m_hot + 100 * Area
Q = U * Area * 30
c1, c2, c3 = st.columns(3)
c1.metric('Predicted U', f'{U:.0f} W/m2K')
c2.metric('Heat Duty Q', f'{Q / 1000:.1f} kW')
c3.metric('Status', 'HEALTHY' if U > 800 else 'FOULING ALERT')
if U < 800:
    st.warning('Fouling alert: U has dropped - schedule cleaning')
else:
    st.success('Exchanger healthy')

df = pd.read_csv('data_monitoring_clean.csv')
st.subheader('Data Table')
st.dataframe(df.head(20))
st.subheader('U vs m_hot')
st.scatter_chart(df, x='m_hot', y='U')
st.subheader('Monthly Saving (USD)')
st.bar_chart(df.groupby('Month')['saving_usd'].sum())
