import streamlit as st
import seaborn as sns
import pandas as pd
import yfinance as yf

st.set_page_config(
    page_title='Data Explorer',
    layout='centered',
    page_icon=':coin:'
)

st.title('My Data Exploration Page')

st.markdown('This is a online data visualization tool for discovering stock data')

option = st.selectbox(
    'Interested stock',
    ('MSFT', 'AAPL', 'COIN'))

ticker = yf.Ticker(option)

time_period = st.slider('What is the historical period (in month) are you interested in?', 1, 36, 1)

hist = ticker.history(period=f"{time_period}mo")

st.dataframe(hist.sort_index(ascending=False))

st.line_chart(hist[['Open', 'High', 'Low', 'Close']])

st.bar_chart(hist[['Volume']])