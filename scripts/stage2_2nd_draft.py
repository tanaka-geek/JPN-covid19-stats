import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime 
import calendar
from meta import *

# Date now has become index
df = pd.read_csv('../covid_jpn_prefecture.csv',  
                 parse_dates=['Date'],
                 index_col=['Date']
)

# Get Active cases in each Prefectures
df['Active_Case'] = df['Positive'] - df['Discharged']

# Get the latest date data now it is 2020 Dec 23rd
data = df.loc[datetime.date(year=2020,month=12,day=23):datetime.date(year=2020,month=12,day=23)]
# data = list(map(lambda x : df.loc[datetime.date(year=2020,month=x,day=1):datetime.date(year=2020,month=x,day=num_days[x])], range(1,12+1)))
#     data[x]['Active_Case'] = data[x]['Positive'].diff().fillna(0)

print(data)

#Get all the Positie Case in Tokyo
print(data.loc[data['Prefecture'] == 'Tokyo', 'Active_Case'].sum())

# The list of all prefectures
prefectures = df.Prefecture.unique()

# Gathering prefecture's total Active_Cases until now
cases_per_prefectures = list({i: data.loc[data['Prefecture'] == i, 'Active_Case'].sum()} for i in prefectures)
# lambda x : cases_per_prefectures[x] = df.loc[df['Prefecture'] == i, 'Active_Case'].sum()
# print(cases_per_prefectures)

# Made sure that we have dict :)
cases = dict()
for i in cases_per_prefectures:
    cases.update(i)

pf = pd.DataFrame(list(cases.items()),columns = ['Prefecture','Active_Case']) 

# Active Cases per each prefecture
print(pf.mean()) # 661 for 47 prefectures 
# Total Active Cases in Japan
print(pf.sum()) # 31112.0
# Median Value : 163 三重県
print(pf.median())


#Get number of days of each month for year 2020
num_days = list(map(lambda month : calendar.monthrange(year, month)[1], range(1,12+1)))

# quick HOT fix
num_days.insert(0,0)
num_days[12-1] = 24

# Categorize cases into each month
data = list(map(lambda x : df.loc[datetime.date(year=2020,month=x,day=1):datetime.date(year=2020,month=x,day=num_days[x])], range(1,12+1)))

for x in range(0,12):
    data[x]['Active_Case'] = data[x]['Positive'].diff().fillna(0)

box = list()
# map(lambda x : box.append(data[x]['Active_Case']), range(0,12))

print(data[2].mean()) #mean
print(data[2].median()) #median
print(data[2]['Active_Case'].max()) #mode

fig1, ax1 = plt.subplots()
ax1.set_title('Test score')
ax1.set_xticklabels(['Math'])
ax1.boxplot(data[3]['Active_Case'])
# plt.axvspan(month['Active_Case'].median()[0],month['Active_Case'].median()[0] , color='red', alpha=0.5)
plt.grid(which='major', alpha=0.5)
# plt.show()



# Add comment 
ax1.text(1,6005, 'Mode Value : 6605 at Tokyo', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
ax1.text(1.15,163, 'Median Value : Mie', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
ax1.boxplot(data['Active_Case'])
ax1.text(1.15,163, 'Median Value : 166 at Mie', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
ax1.boxplot(data['Active_Case'])


### Made a simple list 
k = (data.sum()['Active_Case'])
g = {'Total' : [k]}
print(k)
h = pd.DataFrame(g, columns = ['Total'])
print(h)
# h = pd.DataFrame(list(cases.items()),columns = ['Prefecture','Active_Case']

