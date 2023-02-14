import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple  Stock Price App

Stock price of App 
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='1d', start='2015-5-31', end = '2022-5-31')

st.line_chart(tickerDF.Close)
st.write("""
##Closing Price
""")
st.line_chart(tickerDF.Volume)
st.write("""
##Volume Price
""")