import streamlit as st
import pandas as pd
import binance-futures-connector as cm_futures_client

cm_futures_client = CMFutures()

st.markdown('''# **Binance Futures Price App**
A simple cryptocurrency price app pulling price data from *Binance API*.
''')

st.header('**Selected Price**')

# Load market data from Binance API
df = pd.read_json('https://fapi.binance.com/fapi/v1/ticker/24hr')

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

col1, col2, col3 = st.columns(3)

# Widget (Cryptocurrency selection box)
col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCUSDT') )
col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHUSDT') )
col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBUSDT') )
col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('DOGEUSDT') )
col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADAUSDT') )
col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('AXSUSDT') )
col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBUSDT') )
col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('GALAUSDT') )
col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('NEARUSDT') )

# DataFrame of selected Cryptocurrency
col1_df = df[df.symbol == col1_selection]
col2_df = df[df.symbol == col2_selection]
col3_df = df[df.symbol == col3_selection]
col4_df = df[df.symbol == col4_selection]
col5_df = df[df.symbol == col5_selection]
col6_df = df[df.symbol == col6_selection]
col7_df = df[df.symbol == col7_selection]
col8_df = df[df.symbol == col8_selection]
col9_df = df[df.symbol == col9_selection]

# Apply a custom function to conditionally round values
col1_price = round_value(col1_df.lastPrice)
col2_price = round_value(col2_df.lastPrice)
col3_price = round_value(col3_df.lastPrice)
col4_price = round_value(col4_df.lastPrice)
col5_price = round_value(col5_df.lastPrice)
col6_price = round_value(col6_df.lastPrice)
col7_price = round_value(col7_df.lastPrice)
col8_price = round_value(col8_df.lastPrice)
col9_price = round_value(col9_df.lastPrice)

# Select the priceChangePercent column
col1_percent = f'{float(col1_df.priceChangePercent)}%'
col2_percent = f'{float(col2_df.priceChangePercent)}%'
col3_percent = f'{float(col3_df.priceChangePercent)}%'
col4_percent = f'{float(col4_df.priceChangePercent)}%'
col5_percent = f'{float(col5_df.priceChangePercent)}%'
col6_percent = f'{float(col6_df.priceChangePercent)}%'
col7_percent = f'{float(col7_df.priceChangePercent)}%'
col8_percent = f'{float(col8_df.priceChangePercent)}%'
col9_percent = f'{float(col9_df.priceChangePercent)}%'

# Create a metrics price box
col1.metric(col1_selection, col1_price, col1_percent)
col2.metric(col2_selection, col2_price, col2_percent)
col3.metric(col3_selection, col3_price, col3_percent)
col1.metric(col4_selection, col4_price, col4_percent)
col2.metric(col5_selection, col5_price, col5_percent)
col3.metric(col6_selection, col6_price, col6_percent)
col1.metric(col7_selection, col7_price, col7_percent)
col2.metric(col8_selection, col8_price, col8_percent)
col3.metric(col9_selection, col9_price, col9_percent)

st.header('**All Price**')
st.dataframe(df)

st.info('Credit: Modifed by Sun (aka [SunSamui](https://www.youtube.com/playlist?list=PLNhIISiOZn7XM3thB5YnjRJ-mp_cRMGTl))')

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
