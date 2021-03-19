import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_stats(df_cargo, df_tanker, df_fishing, df_passenger, date_string,
               out_dir, date):
    '''
    Statistics calculation function.
    '''

    df_cargo['date'] = pd.to_datetime(df_cargo['date'], format='%Y%m%d')
    df_tanker['date'] = pd.to_datetime(df_tanker['date'], format='%Y%m%d')
    df_fishing['date'] = pd.to_datetime(df_fishing['date'], format='%Y%m%d')
    df_passenger['date'] = pd.to_datetime(df_passenger['date'], format='%Y%m%d')

    #######
    # date vs types
    #######

    #1
    sns.set_palette("husl")
    concatenated = pd.concat([df_cargo.assign(dataset='df_cargo'), df_tanker.assign(dataset='df_tanker'), df_fishing.assign(dataset="df_fishing"), df_passenger.assign(dataset="df_passenger")])
    g=sns.relplot(x='date', y='Zone_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Zone entry for 4 ship types in {0}".format(date_string))
    plt.savefig('{1}/zone{0}.png'.format(date, out_dir))

    #2
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("AIS Gaps for 4 ship types in  {0}".format(date_string))
    plt.savefig('{1}/gap{0}.png'.format(date, out_dir))

    #3
    g=sns.relplot(x='date', y='Speed_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Speed change for 4 ship types in  {0}".format(date_string))
    plt.savefig('{1}/sc{0}.png'.format(date, out_dir))

    #4
    g=sns.relplot(x='date', y='spd_gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Speed change for 4 ship types in  {0}".format(date_string))
    plt.savefig('{1}/sp_and_gap{0}.png'.format(date, out_dir))

    #5
    g=sns.relplot(x='date', y='all_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Speed change for 4 ship types in  {0}".format(date_string))
    plt.savefig('{1}/sp_and_gap{0}.png'.format(date, out_dir))

    #####
    # date vs anomalies
    #####

    Cargo2=df_cargo[["date","Gap_true","Speed_true","Zone_true"]]
    Fishing2=df_fishing[["date","Gap_true","Speed_true","Zone_true"]]
    Tanker2=df_tanker[["date","Gap_true","Speed_true","Zone_true"]]
    Passenger2=df_passenger[["date","Gap_true","Speed_true","Zone_true"]]

    Cargo3=df_cargo[["spd_gap_true", "all_true"]]
    Fishing3=df_fishing[["spd_gap_true", "all_true"]]
    Tanker3=df_tanker[["spd_gap_true", "all_true"]]
    Passenger3=df_passenger[["spd_gap_true", "all_true"]]

    #1
    plt.clf()
    sns.lineplot(data=Cargo2)
    plt.xlabel("date")
    plt.ylabel("percentage")
    plt.title("Anomalies for Cargo ships in  {0}".format(date_string))
    plt.savefig('{1}/cargo{0}.png'.format(date, out_dir),
                bbox_inches="tight")

    #2
    plt.clf()
    sns.lineplot(data=Tanker2)
    plt.xlabel("date")
    plt.ylabel("percentage")
    plt.title("Anomalies for Tankers in  {0}".format(date_string))
    plt.savefig('{1}/tankers{0}.png'.format(date, out_dir),
                bbox_inches="tight")

    #3
    plt.clf()
    sns.lineplot(data=Fishing2)
    plt.xlabel("date")
    plt.ylabel("percentage")
    plt.title("Anomalies for fishing vessels  {0}".format(date_string))
    plt.savefig('{1}/fish{0}.png'.format(date, out_dir),
                bbox_inches="tight")


    #4
    plt.clf()
    sns.lineplot(data=Passenger2)
    plt.xlabel("date")
    plt.ylabel("percentage")
    plt.title("Anomalies for passenger ships in  {0}".format(date_string))
    plt.savefig('{1}/pass{0}.png'.format(date, out_dir),
                bbox_inches="tight")

    #1
    plt.clf()
    sns.lineplot(data=Cargo3)
    plt.xlabel("date")
    plt.ylabel("percentage")
    plt.title("Anomalies for Cargo ships in  {0}".format(date_string))
    plt.savefig('{1}/cargo{0}_combined.png'.format(date, out_dir),
                bbox_inches="tight")

    #2
    plt.clf()
    sns.lineplot(data=Tanker3)
    plt.xlabel("date")
    plt.ylabel("percentage")
    plt.title("Anomalies for Tankers in  {0}".format(date_string))
    plt.savefig('{1}/tankers{0}_combined.png'.format(date, out_dir),
                bbox_inches="tight")

    #3
    plt.clf()
    sns.lineplot(data=Fishing3)
    plt.xlabel("date")
    plt.ylabel("percentage")
    plt.title("Anomalies for fishing vessels  {0}".format(date_string))
    plt.savefig('{1}/fish{0}_combined.png'.format(date, out_dir),
                bbox_inches="tight")


    #4
    plt.clf()
    sns.lineplot(data=Passenger3)
    plt.xlabel("date")
    plt.ylabel("percentage")
    plt.title("Anomalies for passenger ships in  {0}".format(date_string))
    plt.savefig('{1}/pass{0}_combined.png'.format(date, out_dir))


def compare_stats(df_cargo, df_tanker, df_fishing, df_passenger, date_string,
                  out_dir, date, compare_date, cm_cargo, cm_tanker,
                  cm_fishing, compare_pass):
    #1
    sns.set_palette("husl")
    concatenated = pd.concat([df_cargo.assign(dataset='df_cargo'), cm_cargo.assign(dataset='cm_cargo')])
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Compare AIS gap between 2019 and 2020")
    plt.savefig("Cargo_{0}vs{1}_.png".format(date, compare_date))

    sns.set_palette("husl")
    concatenated = pd.concat([df_tanker.assign(dataset='df_tanker'), cm_tanker.assign(dataset='cm_tanker')])
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Compare AIS gap between 2019 and 2020")
    plt.savefig("tanker_{0}vs{1}_.png".format(date, compare_date))

    sns.set_palette("husl")
    concatenated = pd.concat([df_fishing.assign(dataset='df_fishing'), cm_fishing.assign(dataset='cm_fishing')])
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Compare AIS gap between 2019 and 2020")
    plt.savefig("fishing_{0}vs{1}_.png".format(date, compare_date))

    sns.set_palette("husl")
    concatenated = pd.concat([df_passenger.assign(dataset='df_passenger'), compare_pass.assign(dataset='compare_pass')])
    g=sns.relplot(x='date', y='Gap_true', data=concatenated ,kind='line', hue= 'dataset' , style='dataset')
    g.fig.autofmt_xdate()
    plt.ylabel("percentage")
    plt.title("Compare AIS gap between 2019 and 2020")
    plt.savefig("passenger_{0}vs{1}_.png".format(date, compare_date))
