from datetime import datetime
import pandas as pd
import numpy as np
from extract import PreProcess

prepros = PreProcess()


fmt = '%Y-%m-%d %H:%M:%S'


def search_ais_gaps(df, time):
    minutes = df["# Timestamp"].diff().apply(lambda x: x/np.timedelta64(1, 'm')).fillna(0).astype('int64')
    # timestamp_1 = datetime.strptime(row1[Timestamp], fmt)
    # timestamp_2 = datetime.strptime(row2[Timestamp], fmt)
    # time_delta = (timestamp_2 - timestamp_1)
    # total_seconds = time_delta.total_seconds()
    # minutes = total_seconds/60
    return minutes


def  search_mmsi(df, elem, uniq):
    """Extract all rows from a given MMSI"""
    for val in uniq:
        df_rows_mmsi = prepros.find_rows(df, val, 'MMSI')
        search_ais_gaps(df_rows_mmsi)


# df["Flag"] = "No Problem"
# df.loc[df["minutes"] >= 3, "Flag"] = "Problem"
# df.to_csv("flag_{0}".format(filename))
