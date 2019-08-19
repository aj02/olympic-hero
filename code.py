# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)

data.rename(columns={'Total' : 'Total_Medals'}, inplace=True)

print(data.head())


# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')

data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])

better_event = data['Better_Event'].value_counts().index[0]

print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

# remove last row as it contains sum of values
top_countries = top_countries[:-1]

def top_ten(top_countries, col):
    country_list = []
    country_list = list(top_countries.nlargest(10, col)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = list(set(top_10_summer).intersection(set(top_10_winter)).intersection(set(top_10)))
print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

#print(summer_df.head())

summer_df.plot( kind='bar', x='Country_Name', y='Total_Summer')
plt.xlabel('Country Name')
plt.ylabel('No of Summer Olympic Medals')
plt.xticks(rotation=45)
plt.show()

winter_df.plot( kind='bar', x='Country_Name', y='Total_Winter')
plt.xlabel('Country Name')
plt.ylabel('No of Winter Olympic Medals')
plt.xticks(rotation=45)
plt.show()

top_df.plot( kind='bar', x='Country_Name', y='Total_Medals')
plt.xlabel('Country Name')
plt.ylabel('No of Total Olympic Medals')
plt.xticks(rotation=45)
plt.show()



# --------------
#Code starts here
summer_df

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_gold_ratio_df = summer_df.nlargest(1, 'Golden_Ratio')
summer_country_gold = summer_gold_ratio_df['Country_Name'].iloc[0]
summer_max_ratio = np.round_(summer_gold_ratio_df['Golden_Ratio'].iloc[0], 2)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_gold_ratio_df = winter_df.nlargest(1, 'Golden_Ratio')
winter_country_gold = winter_gold_ratio_df['Country_Name'].iloc[0]
winter_max_ratio = np.round_(winter_gold_ratio_df['Golden_Ratio'].iloc[0], 2)


top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_gold_ratio_df = top_df.nlargest(1, 'Golden_Ratio')
top_country_gold = top_gold_ratio_df['Country_Name'].iloc[0]
top_max_ratio = np.round_(top_gold_ratio_df['Golden_Ratio'].iloc[0], 2)




# --------------
#Code starts here
#print(data)
data_1 = data[:-1]

data_1['Total_Points'] = (data['Gold_Total'] * 3) + (data['Silver_Total'] * 2) + data['Bronze_Total']

top_total_point_df = data_1.nlargest(1, 'Total_Points')

most_points = top_total_point_df['Total_Points'].iloc[0]
best_country = top_total_point_df['Country_Name'].iloc[0]

print(most_points)
print(best_country)


# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

print(best)

best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


