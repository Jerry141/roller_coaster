import pandas as pd
import matplotlib.pyplot as plt

wood_ranking = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_ranking = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
roller_coasters = pd.read_csv('roller_coasters.csv')


# function that plots ranking of a given roller coaster over time
# name - name of the roller coaster
# park - name of the amusement park where the roller coaster is located
# data - dataframe

def rank_year(name, park, data):
    coaster_rankings = data[(data.Name == name) & (data.Park == park)]
    years = [i for i in coaster_rankings['Year of Rank']]
    ranks = [i for i in coaster_rankings['Rank']]

    plt.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'])
    plt.ylabel('Rank')
    plt.xlabel('Year')
    plt.title(f"{name} Rankings")
    ax = plt.subplot()
    ax.set_xticks(years)
    ax.set_yticks(ranks)
    ax.invert_yaxis()
    plt.show()


# function that plots ranking comparison of a given roller coasters over time
# name1 and name 2 - name of the roller coasters to compare
# park1 and park 2 - name of the amusement parks where the roller coasters are located
# data - dataframe


def rank_years_comp(name1, name2, park1, park2, data):
    coaster_rankings1 = data[(data.Name == name1) & (data.Park == park1)]
    coaster_rankings2 = data[(data.Name == name2) & (data.Park == park2)]
    years = [i for i in coaster_rankings1['Year of Rank']]
    ranks = [i for i in coaster_rankings1['Rank']]

    plt.plot(coaster_rankings1['Year of Rank'], coaster_rankings1['Rank'], color='green', label=name1)
    plt.plot(coaster_rankings2['Year of Rank'], coaster_rankings2['Rank'], color='red', label=name2)
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend()
    plt.title(f"{name1} vs. {name2} Rankings")
    ax = plt.subplot()
    ax.set_xticks(years)
    ax.set_yticks(ranks)
    ax.invert_yaxis()
    plt.show()


# function that plots ranking comparison of roller coasters with rank <= n from data dataframe

def rank_top_10(n, data):
    top = data[data['Rank'] <= n]

    fig, ax = plt.subplots(figsize=(10, 10))
    for coaster in set(top['Name']):
        coaster_rankings = top[top['Name'] == coaster].reset_index()
        ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster)
        ax.set_yticks([i for i in range(1, 6)])

        plt.title("Top 10 Rankings")
        plt.xlabel("Year")
        plt.ylabel("Rank")
        plt.legend(loc=4)
    ax.invert_yaxis()
    plt.show()


rank_year("El Toro", "Six Flags Great Adventure", wood_ranking)
plt.clf()
rank_years_comp("El Toro", "Boulder Dash", "Six Flags Great Adventure", "Lake Compounce", wood_ranking)
plt.clf()
rank_top_10(5, wood_ranking)
