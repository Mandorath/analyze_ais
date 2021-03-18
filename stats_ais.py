import pandas as pd


def calc_stats(df, file, col_ais, col_spd, col_zn, unique_col):
    '''
    Statistics calculation function.
    '''
    # df = pd.read_csv(file, delimiter=",")
    # the percentage of "True" in AIS gaps
    percent_gap = df[col_ais].value_counts(normalize=True,
                                           sort=True,
                                           ascending=True
                                           ).mul(100).astype(str)+'%'
    print(percent_gap)
    # the percentage of "True" in speed change
    percent_sc = df[col_spd].value_counts(normalize=True,
                                          sort=True,
                                          ascending=True
                                          ).mul(100).astype(str)+'%'
    print(percent_sc)
    # the percentage of "True" in zone entry with unique MMSI number
    dfc = df[cargo[col_zn] == True]
    group1 = dfc.groupby(unique_col)['Zn_entry'].unique()
    group2 = df[unique_col].unique()
    percentage_zone = len(group1)/len(group2)*100
    print("True:", percentage_zone, "%")
    dfstats = {'Anomaly': ['Gap', 'Speed', 'Zone'],
               'Percentage': [percent_gap, percent_sc, percentage_zone]
               }
    df_out = pd.DataFrame(dfstats, columns=['Anomaly', 'Percentage'])
    return df_out



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
