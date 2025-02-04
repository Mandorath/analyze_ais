import pandas as pd
import numpy as np


def calc_stats(df, col_ais, col_spd, col_zn, unique_col, date, df_out, ship_count):
    '''
    Statistics calculation function.
    '''
    # df = pd.read_csv(file, delimiter=",")
    # the percentage of "True" in AIS gaps
    df['spd_and_gap'] = pd.np.where(df[['flag_spd_chng',
                                        'AIS_G']].eq(True).all(1, skipna=True), True,
                             pd.np.where(df[['flag_spd_chng',
                                             'AIS_G']].isnull().all(1), None,
                                                                        False))
    df['spd_gap_zn'] = pd.np.where(df[['flag_spd_chng',
                                      'AIS_G', 'Zn_entry']].eq(True).all(1, skipna=True), True,
                                      pd.np.where(df[['flag_spd_chng',
                                                      'AIS_G']].isnull().all(1), None,
                                                                        False))
    new_df = df[((df['flag_spd_chng'] == True) & (df['AIS_G'] == True) & (df['Zn_entry'] == True))]
    print(new_df)
    percent_g = df[col_ais].value_counts(normalize=True,
                                           sort=True,
                                           ascending=True
                                           ).mul(100).rename_axis('Gap').reset_index(name='Percentage')
    percentage_gap_true = percent_g.at[0, 'Percentage']
    percentage_gap_false = percent_g.at[1, 'Percentage']
    # the percentage of "True" in speed change
    percent_sc = df[col_spd].value_counts(normalize=True,
                                          sort=True,
                                          ascending=True
                                          ).mul(100).rename_axis('SpeedChange').reset_index(name='Percentage')
    percentage_speed_true = percent_sc.at[0, 'Percentage']
    percentage_speed_false = percent_sc.at[1, 'Percentage']
    # the percentage of "True" in zone entry with unique MMSI number
    dfc = df[df[col_zn] == True]
    group1 = dfc.groupby(unique_col)['Zn_entry'].unique()
    group2 = df[unique_col].unique()
    percentage_zone_true, percentage_zone_false = ((len(group1)/len(group2)*100), (100-(len(group1)/len(group2)*100)))
    percentage_spd_gap = df['spd_and_gap'].value_counts(normalize=True,
                                                        sort=True,
                                                        ascending=True
                                                        ).mul(100).rename_axis('spd_gap').reset_index(name='Percentage')
    print(percentage_spd_gap)
    percentage_spd_gap_t = percentage_spd_gap.at[0, 'spd_gap']
    if not percentage_spd_gap_t:
        percentage_spd_gap_true = 0.0
        percentage_spd_gap_false = percentage_spd_gap.at[0, 'Percentage']
    else:
        percentage_spd_gap_true = percentage_spd_gap.at[0, 'Percentage']
        percentage_spd_gap_false = percentage_spd_gap.at[1, 'Percentage']
    percentage_all = df['spd_gap_zn'].value_counts(normalize=True,
                                                   sort=True,
                                                   ascending=True,
                                                   dropna=False
                                                   ).mul(100).rename_axis('spd_gap_zn').reset_index(name='Percentage')
    print(percentage_all)
    percentage_all_t = percentage_all.at[0, 'spd_gap_zn']
    print(percentage_all_t)
    if not percentage_all_t:
        percentage_all_true = 0.0
        percentage_all_false = percentage_all.at[0, 'Percentage']
    else:
        percentage_all_true = percentage_all.at[0, 'Percentage']
        percentage_all_false = percentage_all.at[1, 'Percentage']
    stats = {'date': [date],
             'Gap_true': [percentage_gap_true],
             'Gap_false': [percentage_gap_false],
             'Speed_true': [percentage_speed_true],
             'Speed_false': [percentage_speed_false],
             'Zone_true': [percentage_zone_true],
             'Zone_false': [percentage_zone_false],
             'spd_gap_true': [percentage_spd_gap_true],
             'spd_gap_false': [percentage_spd_gap_false],
             'all_true': [percentage_all_true],
             'all_false': [percentage_all_false],
             'ship_count': [ship_count]
             }

    dfstats = pd.DataFrame(stats)
    df_t = df_out
    df_t = df_t.append(dfstats, ignore_index=True)
    return df_t, new_df


def create_stats_df():
    dfstats = {'date': [],
               'Gap_true': [],
               'Gap_false': [],
               'Speed_true': [],
               'Speed_false': [],
               'Zone_true': [],
               'Zone_false': [],
               'spd_gap_true': [],
               'spd_gap_false': [],
               'all_true': [],
               'all_false': [],
               'ship_count': []
               }
    df = pd.DataFrame(dfstats)
    return df
# '''
# fishing
# '''
# fish = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Fishing2.out', delimiter = ",")
#
# # the percentage of "True" in AIS gaps
# percent_gap = fish['AIS_G'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
# print(percent_gap)
#
# # the percentage of "True" in speed change
# percent_sc = fish['flag_spd_chng'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
# print(percent_sc)
#
# # the percentage of "True" in zone entry with unique MMSI number
# dff = fish[fish['Zn_entry'] == True]
# group1 = dff.groupby('MMSI')['Zn_entry'].unique()
# group2 = fish['MMSI'].unique()
# percentage_zone= len(group1)/len(group2)*100
# print("True:", percentage_zone,"%")
#
# fishstats = {'Anomaly': ['Gap','Speed','Zone'],
#         'Percentage': [percent_gap,percent_sc,percentage_zone]
#         }
#
# df = pd.DataFrame(fishstats, columns = ['Anomaly', 'Percentage'])
# df.to_csv('fishstats.csv')
# '''
# Tank
# '''
# tank = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Tank2.out', delimiter = ",")
#
# # the percentage of "True" in AIS gaps
# percent_gap = tank['AIS_G'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
# print(percent_gap)
#
# # the percentage of "True" in speed change
# percent_sc = tank['flag_spd_chng'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
# print(percent_sc)
#
# # the percentage of "True" in zone entry with unique MMSI number
# dft = tank[tank['Zn_entry'] == True]
# group1 = dft.groupby('MMSI')['Zn_entry'].unique()
# group2 = tank['MMSI'].unique()
# percentage_zone= len(group1)/len(group2)*100
# print("True:", percentage_zone,"%")
#
# tankstats = {'Anomaly': ['Gap','Speed','Zone'],
#         'Percentage': [percent_gap,percent_sc,percentage_zone]
#         }
#
# df = pd.DataFrame(tankstats, columns = ['Anomaly', 'Percentage'])
# df.to_csv('tankstats.csv')
# '''
# Passenger
# '''
# passenger = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Passenger2.out', delimiter = ",")
#
# # the percentage of "True" in AIS gaps
# percent_gap = passenger['AIS_G'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
# print(percent_gap)
#
# # the percentage of "True" in speed change
# percent_sc = passenger['flag_spd_chng'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
# print(percent_sc)
#
# # the percentage of "True" in zone entry with unique MMSI number
# dfp = passenger[passenger['Zn_entry'] == True]
# group1 = dfp.groupby('MMSI')['Zn_entry'].unique()
# group2 = passenger['MMSI'].unique()
# percentage_zone= len(group1)/len(group2)*100
# print("True:", percentage_zone,"%")
#
# passstats = {'Anomaly': ['Gap','Speed','Zone'],
#         'Percentage': [percent_gap,percent_sc,percentage_zone]
#         }
#
# df = pd.DataFrame(passstats, columns = ['Anomaly', 'Percentage'])
# df.to_csv('passstats.csv')
