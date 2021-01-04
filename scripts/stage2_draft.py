import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime 
import calendar
from meta import *

# Date now has become index
df = pd.read_csv('../datasets/covid_jpn_domestic_total.csv',  
                 parse_dates=['Date'],
                 index_col=['Date']
)

# Add active cases in order to show distgraph of actual active cases 
df['Active_Case'] = df['Positive'] - df['Discharged']

#Get number of days of each month for year 2020
num_days = list(map(lambda month : calendar.monthrange(year, month)[1], range(1,12+1)))

# quick HOT fix
num_days.insert(0,0)
num_days[12-1] = 24

# Categorize cases into each month
data = list(map(lambda x : df.loc[datetime.date(year=2020,month=x,day=1):datetime.date(year=2020,month=x,day=num_days[x])], range(1,12+1)))

for x in range(0,12):
    data[x]['Daily_Increase'] = data[x]['Positive'].diff().fillna(0)

box = list()
# map(lambda x : box.append(data[x]['Daily_Increase']), range(0,12))

print(data[2].mean()) #mean
print(data[2].median()) #median
print(data[2]['Daily_Increase'].max()) #mode

fig1, ax1 = plt.subplots()
ax1.set_title('Test score')
ax1.set_xticklabels(['Math'])
ax1.boxplot(data[3]['Daily_Increase'])
# plt.axvspan(month['Active_Case'].median()[0],month['Active_Case'].median()[0] , color='red', alpha=0.5)
plt.grid(which='major', alpha=0.5)
plt.show()