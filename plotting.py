import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_stats(cargo, tanker, fishing, passenger, date_string,
               out_dir, date):
    '''
    Statistics calculation function.
    '''

    cargo['date'] = pd.to_datetime(cargo['date'], format='%Y%m%d')
    tanker['date'] = pd.to_datetime(tanker['date'], format='%Y%m%d')
    fishing['date'] = pd.to_datetime(fishing['date'], format='%Y%m%d')
    passenger['date'] = pd.to_datetime(passenger['date'], format='%Y%m%d')

    #######
    # date vs types
    #######

    #1
    sns.set_palette("husl")
    concatenated = pd.concat([cargo.assign(dataset='cargo'), tanker.assign(dataset='tanker'), fishing.assign(dataset="fishing"), passenger.assign(dataset="passenger")])
    g=sns.relplot(x='date', y='Zone_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Zone entry for 4 ship types in {0}".format(date_string))
    plt.savefig('{1}/zone{0}.png'.format(date, out_dir), bbox_inches="tight")

    #2
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("Percentage of vessels p/d")
    plt.title("AIS Gaps for 4 ship types in  {0}".format(date_string))
    plt.savefig('{1}/gap{0}.png'.format(date, out_dir), bbox_inches="tight")

    #3
    g=sns.relplot(x='date', y='Speed_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Speed change for 4 ship types in  {0}".format(date_string))
    plt.savefig('{1}/sc{0}.png'.format(date, out_dir), bbox_inches="tight")

    #4
    g=sns.relplot(x='date', y='spd_gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Speed and Gap combined {0}".format(date_string))
    plt.savefig('{1}/sp_and_gap{0}.png'.format(date, out_dir), bbox_inches="tight")

    #5
    g=sns.relplot(x='date', y='all_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("Percentage of vessels p/d")
    plt.title("All anomalies {0}".format(date_string))
    plt.savefig('{1}/all_true_{0}.png'.format(date, out_dir), bbox_inches="tight")

    #####
    # date vs anomalies
    #####

    Cargo2=cargo[["date","Gap_true","Speed_true","Zone_true"]]
    Fishing2=fishing[["date","Gap_true","Speed_true","Zone_true"]]
    Tanker2=tanker[["date","Gap_true","Speed_true","Zone_true"]]
    Passenger2=passenger[["date","Gap_true","Speed_true","Zone_true"]]

    Cargo3=cargo[["spd_gap_true", "all_true"]]
    Fishing3=fishing[["spd_gap_true", "all_true"]]
    Tanker3=tanker[["spd_gap_true", "all_true"]]
    Passenger3=passenger[["spd_gap_true", "all_true"]]

    #1
    plt.clf()
    sns.lineplot(data=Cargo2)
    plt.xlabel("date")
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Anomalies for Cargo ships in  {0}".format(date_string))
    plt.savefig('{1}/cargo{0}.png'.format(date, out_dir),
                bbox_inches="tight")

    #2
    plt.clf()
    sns.lineplot(data=Tanker2)
    plt.xlabel("date")
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Anomalies for Tankers in  {0}".format(date_string))
    plt.savefig('{1}/tankers{0}.png'.format(date, out_dir),
                bbox_inches="tight")

    #3
    plt.clf()
    sns.lineplot(data=Fishing2)
    plt.xlabel("date")
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Anomalies for fishing vessels  {0}".format(date_string))
    plt.savefig('{1}/fish{0}.png'.format(date, out_dir),
                bbox_inches="tight")


    #4
    plt.clf()
    sns.lineplot(data=Passenger2)
    plt.xlabel("date")
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Anomalies for passenger ships in  {0}".format(date_string))
    plt.savefig('{1}/pass{0}.png'.format(date, out_dir),
                bbox_inches="tight")

    #1
    plt.clf()
    sns.lineplot(data=Cargo3)
    plt.xlabel("date")
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Anomalies for Cargo ships in  {0}".format(date_string))
    plt.savefig('{1}/cargo{0}_combined.png'.format(date, out_dir),
                bbox_inches="tight")

    #2
    plt.clf()
    sns.lineplot(data=Tanker3)
    plt.xlabel("date")
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Anomalies for Tankers in  {0}".format(date_string))
    plt.savefig('{1}/tankers{0}_combined.png'.format(date, out_dir),
                bbox_inches="tight")

    #3
    plt.clf()
    sns.lineplot(data=Fishing3)
    plt.xlabel("date")
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Anomalies for fishing vessels  {0}".format(date_string))
    plt.savefig('{1}/fish{0}_combined.png'.format(date, out_dir),
                bbox_inches="tight")


    #4
    plt.clf()
    sns.lineplot(data=Passenger3)
    plt.xlabel("date")
    plt.ylabel("Percentage of vessels p/d")
    plt.title("Anomalies for passenger ships in  {0}".format(date_string))
    plt.savefig('{1}/pass{0}_combined.png'.format(date, out_dir),
                bbox_inches="tight")


def compare_stats(cargo, tanker, fishing, passenger, date_string,
                  out_dir, date, compare_date, cm_cargo, cm_tanker,
                  cm_fishing, compare_pass):
    #1
    plt.clf()
    sns.set_palette("husl")
    concatenated = pd.concat([cargo.assign(dataset='cargo'), cm_cargo.assign(dataset='cm_cargo')])
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Compare AIS gap between 2019 and 2020")
    plt.savefig("{2}/Cargo_{0}vs{1}_.png".format(date, compare_date, out_dir))

    plt.clf()
    sns.set_palette("husl")
    concatenated = pd.concat([tanker.assign(dataset='tanker'), cm_tanker.assign(dataset='cm_tanker')])
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Compare AIS gap between 2019 and 2020")
    plt.savefig("{2}/tanker_{0}vs{1}_.png".format(date, compare_date, out_dir))

    plt.clf()
    sns.set_palette("husl")
    concatenated = pd.concat([fishing.assign(dataset='fishing'), cm_fishing.assign(dataset='cm_fishing')])
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Compare AIS gap between 2019 and 2020")
    plt.savefig("{2}/fishing_{0}vs{1}_.png".format(date, compare_date, out_dir))

    plt.clf()
    sns.set_palette("husl")
    concatenated = pd.concat([passenger.assign(dataset='passenger'), compare_pass.assign(dataset='compare_pass')])
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Compare AIS gap between 2019 and 2020")
    plt.savefig("{2}/passenger_{0}vs{1}_.png".format(date, compare_date, out_dir))
