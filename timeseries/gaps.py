import pandas as pd
from datetime import datetime, timedelta

def get_timeseries_gaps(df, timestamp_col, threshold, drop_orig_index=True):
    """
    Identify gaps based in a value (typically timeseries data) based on a threshold.
    
    :param df: a pandas dataframe
    :param timestamp_col: column being inspected
    :param threshold: size of gaps to look for
    :param drop_orig_index: Defults to True. This function will reset the index of df. To preserve the origonal index
    within the returned value, set this to False.
    """
    df = df.sort_values(by=timestamp_col)
    df.reset_index(inplace=True, drop=drop_orig_index)
    df['{}_diff'.format(timestamp_col)] = df[timestamp_col].diff()
    return df[df['{}_diff'.format(timestamp_col)] >= threshold]
