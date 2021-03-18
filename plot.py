import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Cargo = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Cargo_stats.out', delimiter = ",")
Tanker = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Tanker_stats.out', delimiter = ",")
Fishing = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Fishing_stats.out', delimiter = ",")
Passenger = pd.read_csv('/Users/caseywong/Documents/GitHub/analyze_ais/Passenger2.out', delimiter = ",")

Cargo['date'] = pd.to_datetime(Cargo['date'], format='%Y%m%d')
Tanker['date'] = pd.to_datetime(Tanker['date'], format='%Y%m%d')
Fishing['date'] = pd.to_datetime(Fishing['date'], format='%Y%m%d')
Passenger['date'] = pd.to_datetime(Passenger['date'], format='%Y%m%d')

#######
# date vs types
#######

#1
sns.set_palette("husl")
concatenated = pd.concat([Cargo.assign(dataset='Cargo'), Tanker.assign(dataset='Tanker'), Fishing.assign(dataset="Fishing"), Passenger.assign(dataset="Passenger")])
g=sns.relplot(x='date', y='Zone_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
g.fig.autofmt_xdate()
plt.ylabel("percentage")
plt.title("Zone entry for 4 ship types in July 2020")
plt.show()

#2
g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
g.fig.autofmt_xdate()
plt.ylabel("percentage")
plt.title("AIS Gaps for 4 ship types in July 2020")
plt.show()

#3
g=sns.relplot(x='date', y='Speed_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
g.fig.autofmt_xdate()
plt.ylabel("percentage")
plt.title("Speed change for 4 ship types in July 2020")
plt.show()

#####
# date vs anomalies
#####

Cargo2=Cargo[["date","Gap_true","Speed_true","Zone_true"]]
Fishing2=Fishing[["date","Gap_true","Speed_true","Zone_true"]]
Tanker2=Tanker[["date","Gap_true","Speed_true","Zone_true"]]
Passenger2=Passenger[["date","Gap_true","Speed_true","Zone_true"]]

#1
sns.lineplot(data=Cargo2)
plt.xlabel("date")
plt.ylabel("percentage")
plt.title("Anomalies for Cargo ships in July 2020")
plt.show()

#2
sns.lineplot(data=Tanker2)
plt.xlabel("date")
plt.ylabel("percentage")
plt.title("Anomalies for Tankers in July 2020")
plt.show()

#3
sns.lineplot(data=Fishing2)
plt.xlabel("date")
plt.ylabel("percentage")
plt.title("Anomalies for fishing vessels in July 2020")
plt.show()

#4
sns.lineplot(data=Passenger2)
plt.xlabel("date")
plt.ylabel("percentage")
plt.title("Anomalies for passenger ships in July 2020")
plt.show()