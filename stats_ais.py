import pandas as pd

'''
Cargo2.out file
'''
cargo = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Cargo2.out', delimiter = ",")

# the percentage of "True" in AIS gaps
percent_gap = cargo['AIS_G'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
print(percent_gap)

# the percentage of "True" in speed change
percent_sc = cargo['flag_spd_chng'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
print(percent_sc)

# the percentage of "True" in zone entry with unique MMSI number
dfc = cargo[cargo['Zn_entry'] == True]
group1 = dfc.groupby('MMSI')['Zn_entry'].unique()
group2 = cargo['MMSI'].unique()
percentage_zone= len(group1)/len(group2)*100
print("True:", percentage_zone,"%")

'''
fishing
'''
fish = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Fishing2.out', delimiter = ",")

# the percentage of "True" in AIS gaps
percent_gap = fish['AIS_G'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
print(percent_gap)

# the percentage of "True" in speed change
percent_sc = fish['flag_spd_chng'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
print(percent_sc)

# the percentage of "True" in zone entry with unique MMSI number
dff = fish[fish['Zn_entry'] == True]
group1 = dff.groupby('MMSI')['Zn_entry'].unique()
group2 = fish['MMSI'].unique()
percentage_zone= len(group1)/len(group2)*100
print("True:", percentage_zone,"%")

'''
Tank
'''
tank = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Tank2.out', delimiter = ",")

# the percentage of "True" in AIS gaps
percent_gap = tank['AIS_G'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
print(percent_gap)

# the percentage of "True" in speed change
percent_sc = tank['flag_spd_chng'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
print(percent_sc)

# the percentage of "True" in zone entry with unique MMSI number
dft = tank[tank['Zn_entry'] == True]
group1 = dft.groupby('MMSI')['Zn_entry'].unique()
group2 = tank['MMSI'].unique()
percentage_zone= len(group1)/len(group2)*100
print("True:", percentage_zone,"%")

'''
Passenger
'''
passenger = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Passenger2.out', delimiter = ",")

# the percentage of "True" in AIS gaps
percent_gap = passenger['AIS_G'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
print(percent_gap)

# the percentage of "True" in speed change
percent_sc = passenger['flag_spd_chng'].value_counts(normalize=True,sort=True, ascending=True).mul(100).astype(str)+'%'
print(percent_sc)

# the percentage of "True" in zone entry with unique MMSI number
dfp = passenger[passenger['Zn_entry'] == True]
group1 = dfp.groupby('MMSI')['Zn_entry'].unique()
group2 = passenger['MMSI'].unique()
percentage_zone= len(group1)/len(group2)*100
print("True:", percentage_zone,"%")