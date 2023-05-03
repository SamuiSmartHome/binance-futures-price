import streamlit as st
import pandas as pd

st.markdown('''# **Binance Futures Price App**
A simple cryptocurrency price app pulling price data from *Binance API*.
''')

st.header('**Selected Price**')

# Load market data from Binance API
df = pd.read_json('https://fapi.binance.com/fapi/v1/ticker/24hr?symbol=')

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

crpytoList = {
    'Price 1': 'BTCUSDT',
    'Price 2': 'ETHUSDT',
    'Price 3': 'BNBUSDT',
    'Price 4': 'DOGEUSDT',
    'Price 5': 'ADAUSDT',
    'Price 6': 'AXSUSDT',
    'Price 7': 'SHIBUSDT',
    'Price 8': 'GALAUSDT',
    'Price 9': 'NEARUSDT'
}

col1, col2, col3 = st.columns(3)

for i in range(len(crpytoList.keys())):
   selected_crypto_label = list(crpytoList.keys())[i]
   selected_crypto_index = list(df.symbol).index(crpytoList[selected_crypto_label])
    selected_crypto = st.sidebar.selectbox(selected_crypto_label, df.symbol, selected_crypto_index, key = str(i))
    col_df = df[df.symbol == selected_crypto]
    col_price = round_value(col_df.lastPrice)
    col_percent = f'{float(col_df.priceChangePercent)}%'
    if i < 3:
        with col1:
            st.metric(selected_crypto, col_price, col_percent)
    if 2 < i < 6:
        with col2:
            st.metric(selected_crypto, col_price, col_percent)
    if i > 5:
        with col3:
            st.metric(selected_crypto, col_price, col_percent)

st.header('**All Price**')
st.dataframe(df)

st.info('Credit: Modifed by Sun (aka [SunSamui](https://www.youtube.com/playlist?list=PLNhIISiOZn7XM3thB5YnjRJ-mp_cRMGTl))')

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
