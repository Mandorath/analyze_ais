from datetime import datetime
import pandas as pd
import numpy as np
from extract import PreProcess
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import geopandas as gpd
import fun_logger

log = fun_logger.init_log()
prepros = PreProcess()


fmt = '%Y-%m-%d %H:%M:%S'

class AnalyzeDf():

    def search_ais_gaps(self, df, column, time):
        """
        Search for (large) gaps in time.

        Search for (large) gaps per the current and last row in the df.
        When a gap is larger then the specified time it will be flagged.

        Args:
        ----
            df (df): Pandas dataframe.
            column (str): Column to use for the comparison.
            time (int): Time to check the gap with.

        """
        # Make the column a proper time_stamp instead of str/int
        AIS_Gap = time
        df_ret = df
        df_t = pd.DataFrame()
        df_t[column] = pd.to_datetime(df[column])
        df_ret['T_Gap'] = df_t[column].diff().apply(lambda x: x/np.timedelta64(1, 'm')).fillna(0).astype('int64')
        # timestamp_1 = datetime.strptime(row1[Timestamp], fmt)
        # timestamp_2 = datetime.strptime(row2[Timestamp], fmt)
        # time_delta = (timestamp_2 - timestamp_1)
        # total_seconds = time_delta.total_seconds()
        # minutes = total_seconds/60
        df_ret['AIS_G'] = df_ret['T_Gap'] > AIS_Gap
        return df_ret

    # Source: https://stackoverflow.com/questions/37063038/how-to-compare-multiple-rows-from-same-column-in-dataframe
    # speed = df[column].diff(1).rolling(w_size).apply(lambda spd: True if ((spd / spd) * 100) > percent else False).fillna(0).astype(bool)
    def grad_change(self, df, column, w_size):
        """
        Calculate the gradual increase/decrease of each row.

        Calculate the gradual increase/decrease of each row in the specified
        column, based on a specified window. Window determines how many rows
        will be used to calculate an average increase/decrease.

        Args:
        ----
            df (df): Pandas dataframe
            column (str): Column to use for the comparison
            w_size (int): Window size to use

        """
        # Compare this many rows for gradual increase/decrease
        w_size = w_size + 1
        # We could still construe this as an invalid measurement, e.g. due to a
        # a fault the speed drops/increases drastically this will distort the
        # average, we could do a percentage check for each value and then check
        # if there are unreasonable speed changes and then drop/ingore those
        df_av = pd.DataFrame()
        df_ret = df
        for i in range(1, w_size):
            df_av['gr_pct{0}'.format(i)] = df[column].pct_change(periods=i)
        df_ret['gr_prct'] = df_av.sum(axis=1) / len(df.columns)
        return df_ret

    def perc_change_incr(self, df, column, l_perc, h_perc):
        """
        Check if a value falls between the defined lower and upper bound.

        Args:
        ----
            df (df): Pandas dataframe
            column (str): Column to use for the comparison
            l_perc (float): Lower bound value to use.
            h_perc (float): Upper bound value to use.

        """
        df_ret = df
        df['abs'] = df[column].abs()
        # df[column] = pd.to_numeric(df[column], downcast="float")
        df_ret['flag_spd_chng'] = df['abs'].between(l_perc, h_perc,
                                                    inclusive=True)
        # df.join(df_ret['h_incr'])
        return df_ret

    def perc_change_decr(self, df, column, l_perc, h_perc):
        """
        Check if a value falls between the defined lower and upper bound.

        Args:
        ----
            df (df): Pandas dataframe
            column (str): Column to use for the comparison
            l_perc (float): Lower bound value to use.
            h_perc (float): Upper bound value to use.

        """
        df_ret = df
        df_ret[column] = df_ret[column].abs()
        df_ret['h_decr'] = df[column].between(l_perc, h_perc, inclusive=True)
        return df_ret

    # Source: https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python
    def setup_polygon(self, list_coordinates):
        """
        Create a polygon based on the provided coordinates.

        Args:
        ----
            list_coordinates: List containing long/lat coordinates.

        """
        poly = Polygon(list_coordinates)
        return poly

    def check_in_polygon(self, df, polygon):
        """
        Check if a set of lat/long coordinates is within the provided polygon.

        Args:
        ----
            df: Pandas dataframe
            polygon: Polygon created based on a list of lat/long coordinates.

        """
        # df_geo['geometry'] = df.apply(lambda x: Point([x['Longtitude', x['Latitude']], axis=1)
        gdf = gpd.GeoDataFrame(
              df, geometry=gpd.points_from_xy(
                                     df.Longitude,
                                     df.Latitude))
        data_poly = gpd.read_file(polygon)
        within = gpd.sjoin(gdf, data_poly, how='inner', op='within')
        outside = gpd.sjoin(gdf, data_poly, how='left', op='within')
        if not within.empty and not outside.empty:
            within['Zn_entry'] = True
            outside['Zn_entry'] = False
            joined_gdf = pd.concat([within, outside])
            print(joined_gdf)
        elif within.empty and not outside.empty:
            outside['Zn_entry'] = False
            joined_gdf = outside
            print(joined_gdf)
        elif not within.empty and outside.empty:
            within['Zn_entry'] = True
            joined_gdf = within
            print(joined_gdf)
        else:
            log.error("Both gdfs are empty which should not happen!")

        # joined_gdf = gpd.sjoin(gdf, data_poly, op='within')
        return joined_gdf


#  def  search_mmsi(df, elem, uniq):
#     """Extract all rows from a given MMSI"""
#     for val in uniq:
#         df_rows_mmsi = prepros.find_rows(df, val, 'MMSI')
#         search_ais_gaps(df_rows_mmsi)


# df["Flag"] = "No Problem"
# df.loc[df["minutes"] >= 3, "Flag"] = "Problem"
# df.to_csv("flag_{0}".format(filename))
# 10.7049484, 57.2991812
# 10.7559174, 57.1201724
# 11.0608432, 56.9798264
# 11.4042281, 57.3371066
# 10.7092171, 57.3044995
