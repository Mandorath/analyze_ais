from datetime import datetime
import pandas as pd

fmt = '%Y-%m-%d %H:%M:%S'
timestamp_1 = datetime.strptime(row1[Timestamp], fmt)
timestamp_2 = datetime.strptime(row2[Timestamp], fmt)

def search_ais_gaps(minutes):
    uniq = prepros.extract_uniq_val(df, 'MMSI')
    time_delta = (timestamp_2 - timestamp_1)
    total_seconds = time_delta.total_seconds()
    minutes = total_seconds/60
    return minutes

def  search_mmsi(df, elem, uniq):
    for val in uniq:
    uniq = prepros.extract_uniq_val(df, 'MMSI')
    df_rows_mmsi = prepros.find_rows(df, val, 'MMSI')       
    search_ais_gaps(df_rows_mmsi)


df["Flag"] = "No Problem"
df.loc[df["minutes"] >= 3, "Flag"] = "Problem"
df.to_csv("flag_{0}".format(filename))