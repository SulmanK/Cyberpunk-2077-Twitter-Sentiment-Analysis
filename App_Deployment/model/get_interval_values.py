#--------------------- Packages
import pandas as pd

#--------------------- Interval Values
def get_value(df, n_intervals):
    """Function which outputs the tweet text given the interval for live updates"""
    text = df['tweet'][n_intervals]
    return text