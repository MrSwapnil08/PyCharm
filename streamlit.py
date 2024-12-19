import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv')

st.write('Original Data', data)

missing_data = data.isnull().sum().reset_index()
missing_data.columns = ['Column', 'Missing Values']

st.write('Missing Values', missing_data)
