import pandas as pd
import data_aggregator as da


def read_data_from_csv(filename):
    """
    Read data from csv file
    :param filename:
    :return:
    """
    df = pd.read_csv(filename)
    return df
