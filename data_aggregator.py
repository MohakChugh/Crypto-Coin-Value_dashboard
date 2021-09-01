import streamlit as st
import requests
import pandas as pd


@st.cache
def get_coin_data_from_api() -> dict:
    """
    Gets data from coinmarketcap.com and returns a dictionary with the data.
    """

    url = 'http://api.coinlayer.com/api/live?access_key=be0b835054010e21fed19b1901410769'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('Error:', response.status_code)
        return None


@st.cache
def create_dataframe(data: dict) -> pd.DataFrame:
    """
    Creates a pandas dataframe from the dictionary.
    """
    df = pd.DataFrame(data)
    df.index.name = 'coin_name'
    return df


@st.cache
def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the dataframe.
    """
    # Drop the columns that are not needed.
    data = data.drop(['success', 'terms', 'privacy',
                     'timestamp', 'target'], axis=1)
    return data


@st.cache
def save_dataframe_to_csv(data: pd.DataFrame, filename: str) -> bool:
    """
    Saves the dataframe to a csv file.
    """
    try:
        data = clean_data(data)
        data.to_csv(filename)
        return True
    except(FileNotFoundError):
        print('Error: Could not save the dataframe to csv.')
        return False


@st.cache
def get_coin_names() -> list:
    """
    Returns a list of all coin names.
    """
    df = read_data_from_csv('data_aggregator.csv')
    return df['coin_name'].to_list()


@st.cache
def read_data_from_csv(filename: str) -> pd.DataFrame:
    """
    Reads the data from a csv file.
    """
    try:
        data = pd.read_csv(filename)
        return data
    except(FileNotFoundError):
        print('Error: Could not read the data from csv.')
        return None


@st.cache
def get_coin_price(df: pd.DataFrame, coin_name: str) -> float:
    """
    Returns the price of a coin.
    """
    try:
        return df[(df['coin_name'] == coin_name)]['rates'].values[0]
    except(IndexError):
        print('Error: Could not find the coin.')
        return None


@st.cache
def get_coin_price_list(df: pd.DataFrame) -> list:
    """
    Returns a list of all coin prices.
    """
    return df['rates'].to_list()

