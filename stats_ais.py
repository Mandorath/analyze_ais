import pandas as pd


def calc_stats(df, col_ais, col_spd, col_zn, unique_col, date, df_out):
    '''
    Statistics calculation function.
    '''
    # df = pd.read_csv(file, delimiter=",")
    # the percentage of "True" in AIS gaps
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
    print(df)
    dfc = df[df[col_zn] == True]
    group1 = dfc.groupby(unique_col)['Zn_entry'].unique()
    group2 = df[unique_col].unique()
    percentage_zone_true, percentage_zone_false = ((len(group1)/len(group2)*100), (100-(len(group1)/len(group2)*100)))

    dfstats = {'date': date,
               'Gap_true': percentage_gap_true,
               'Gap_false': percentage_gap_false,
               'Speed_true': percentage_speed_true,
               'Speed_false': percentage_speed_false,
               'Zone_true': percentage_zone_true,
               'Zone_false': percentage_zone_false,
               }

    df_out = df_out.append(dfstats)
    return df_out


def create_stats_df():
    dfstats = {'date': [],
               'Gap_true': [],
               'Gap_false': [],
               'Speed_true': [],
               'Speed_false': [],
               'Zone_true': [],
               'Zone_false': [],
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
