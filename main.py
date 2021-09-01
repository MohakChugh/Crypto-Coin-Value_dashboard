import streamlit as st
import utils as ut
import pandas as pd
import data_aggregator as da

st.write("# Crypto Coin Prices in USD")
st.write(ut.read_data_from_csv('data_aggregator.csv'))

refresh_data = st.button("Refresh Data")
data_frame = da.read_data_from_csv('data_aggregator.csv')

if refresh_data:
    da.save_dataframe_to_csv(da.create_dataframe(da.get_coin_data_from_api()), 'data_aggregator.csv')
    st.write("Data refreshed")

st.sidebar.title("Coin Selections")
st.sidebar.subheader("Select coins to view")
coin_selected = st.sidebar.selectbox("Select coins", da.get_coin_names())

st.write("Coin Selected: ", coin_selected)
st.write("Price: ", da.get_coin_price(data_frame, coin_selected), "USD")

st.line_chart(pd.DataFrame(da.get_coin_names(), da.get_coin_price_list(data_frame)))
