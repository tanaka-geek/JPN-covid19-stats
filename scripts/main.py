import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Date now has become index
df = pd.read_csv('../covid_jpn_domestic_total.csv',  
                 parse_dates=['Date'],
                 index_col=['Date']
)
# Add active cases in order to show distgraph of actual active cases 
df['Active_Case'] = df['Positive'] - df['Discharged']

# df_a = pd.DataFrame({'Date' : pd.to_datetime(df.index.values)},index=df)

# print(df_a.head())

# df_Month = df.month
month = df.resample(rule="M").mean()
print(month['Active_Case']) #月ごとの平均値

print(month['Active_Case'].mode()) 

print(month['Active_Case'].median()) 

# # Create figure and plot space
# fig, ax = plt.subplots(figsize=(10, 10))

# # Add x-axis and y-axis
# ax.plot(df.index.values,
#         df['Fatal'],
#         linestyle="--",
#         color='red',
#         label="Death Toll",
#         )

# # Set title and labels for axes
# # ax.set(xlabel="Date",
# #        ylabel="",
# #        title="",
# #        label="Death Toll")

# # Rotate tick marks on x-axis
# plt.setp(ax.get_xticklabels(), rotation=45)


# # df = sns.load_dataset('../covid_jpn_total.csv')
# sns.lineplot(df.index.values, df['Active_Case'], ci='sd', data=df, label="Active Cases")
# # sns.distplot(df['Fatal'], label="Fatal", bins=30,kde=False)
# # sns.set(style='dark')

# plt.title('Total Covid-19 Cases in Japan')
# plt.xlabel("Date")
# plt.ylabel("Active Cases")

# # 線が足されるので、良い
# plt.grid()
# fig.tight_layout()
# plt.show()

# # fig, ax = plt.subplots(figsize=(10,10))

# # #Add x-axis and y-axis
# # ax.plot(df.index.values,
# #         df['Active_Case'])

# # # Set title and lables for axes
# # ax.set(xlabel="Date",
# #        ylabel="Positive Case",
# #        title="Covid-19 Cases")

# # plt.show()


# # print(df.head())


################################## STAGE 2 ###################################
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime 
import calendar
from meta import *

# Date now has become index
df = pd.read_csv('../covid_jpn_domestic_total.csv',  
                 parse_dates=['Date'],
                 index_col=['Date']
)

# Add active cases in order to show distgraph of actual active cases 
df['Active_Case'] = df['Positive'] - df['Discharged']

# Obtain resampled data to formulate montly sum
# month = df.resample(rule="M").mean()

# print(month['Active_Case']) #月ごとの平均値
# print(month['Active_Case'].mode()) 
#print(month['Active_Case'])

#sns.catplot(data=month, kind='box', x=month.index.values, y=month['Active_Case'])

#print(month['Active_Case'].median())

# fig, ax = plt.subplots(figsize=(10, 10))
# bp = ax.boxplot(month['Active_Case'])
# ax.bar(month.index.values, month['Active_Case'], width=20.0 )

Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# result = df.Date.str.extractall(r'(2020-02.*)')

# print(result[0:100])

# filter_col = [col for col in df['Date'] if col.startswith(r'(2020-02.*)')]
# df2 = df[(df['Date'] == r'(2020-02.*)')]

# print(filter_col)

#Get number of days of each month for year 2020
num_days = list(map(lambda month : calendar.monthrange(year, month)[1], range(1,12+1)))

# quick HOT fix
num_days.insert(0,0)
num_days[12-1] = 24
# THIS IS THE LINE THAT WORKED

data = list(map(lambda x : df.loc[datetime.date(year=2020,month=x,day=1):datetime.date(year=2020,month=x,day=num_days[x])], range(1,12+1)))

# print(df.filter(regex=r'2020-02.*'))
for x in range(0,12):
    data[x]['Active_Case'] = data[x]['Positive'] - data[x]['Discharged']
    data[x]['Daily_Increase'] = data[x]['Active_Case'].diff().fillna(0)



box = list()
# map(lambda x : box.append(data[x]['Daily_Increase']), range(0,12))


# print(data[3])
# print(box[0])
# # map(lambda x : box.append(list(data[x]['Daily_Increase'])), range(0,12))
# print(box)

# df.shape[0] is number of row count
# fig1, ax1 = plt.subplots()
# ax1.set_title('Test score')
# ax1.set_xticklabels(['Math'])
# ax1.boxplot(data['Daily_Increase'])
# # plt.axvspan(month['Active_Case'].median()[0],month['Active_Case'].median()[0] , color='red', alpha=0.5)
# plt.grid(which='major', alpha=0.5)
# plt.show()