import streamlit as st
import seaborn as sns
import pandas as pd
import yfinance as yf
import pytz
from datetime import datetime
import time 

st.set_page_config(
    page_title='Data Explorer',
    layout='centered',
    page_icon=':coin:'
)

st.title('Financial Data Explorer')

st.markdown('This is a online data visualization tool for discovering stock data, implemented by Matthew Zhang')

with st.sidebar:

    option = st.selectbox(
        'Interested stock',
        ('MSFT', 'AAPL', 'COIN'))

    ticker = yf.Ticker(option)

    time_period = st.slider('What is the historical period (in month) are you interested in?', 1, 36, 1)

    

hist = ticker.history(period=f"{time_period}mo")

st.dataframe(hist.sort_index(ascending=False))

st.line_chart(hist[['Open', 'High', 'Low', 'Close']])

st.bar_chart(hist[['Volume']])


st.header('World Clock')

cities = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Berlin": "Europe/Berlin",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Mumbai": "Asia/Kolkata",
}

# Let users select multiple cities from the list
selected_cities = st.multiselect('Select cities', options=list(cities.keys()))

# Placeholder for live clock
clock_placeholder = st.empty()

while True:
    # Display the current time for each selected city
    time_str = ""
    for city in selected_cities:
        timezone = pytz.timezone(cities[city])
        city_time = datetime.now(timezone)
        time_str += f"{city}: {city_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    clock_placeholder.markdown(time_str)
    
    # Wait for a second before updating the clock
    time.sleep(1)