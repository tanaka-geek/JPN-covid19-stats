import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime 
import calendar
from meta import *

# Date now has become index
df = pd.read_csv('../datasets/covid_jpn_prefecture.csv',  
                 parse_dates=['Date'],
                 index_col=['Date']
)

# Get Active cases in each Prefectures
df['Active_Case'] = df['Positive'] - df['Discharged']

# Get the latest date data now it is 2020 Dec 23rd
data = df.loc[datetime.date(year=2020,month=12,day=23):datetime.date(year=2020,month=12,day=23)]

# Active Cases per each prefecture
mean_data = data.mean() # 661 for 47 prefectures 
# Total Active Cases in Japan
sum_data = data.sum() # 31112.0
# Median Value : 163 三重県
median_data = data.median()
# mode, based on the most positive Cases
mode_data = (data.loc[data['Positive'] == data['Positive'].max()])

# Drop Unnecessary Data such as 'Tested'
mean_data = mean_data.drop(['Tested'])
sum_data = sum_data.drop(['Tested'])
median_data = median_data.drop(['Tested'])
mode_data = mode_data

# print put mean,median and mode 
mean_value = mean_data.Positive
median_value =median_data.Positive
mode_value = mode_data.Positive[0]

f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw= {"height_ratios": (0.2, 1)})

sns.boxplot(data["Positive"], ax=ax_box)
ax_box.axvline(mean_value, color='r', linestyle='--')
ax_box.axvline(median_value, color='g', linestyle='-')
ax_box.axvline(mode_value, color='b', linestyle='-')

sns.distplot(data["Positive"], ax=ax_hist)
ax_hist.axvline(mean_value, color='r', linestyle='--')
ax_hist.axvline(median_value, color='g', linestyle='-')
ax_hist.axvline(mode_value, color='b', linestyle='-')

# Adding labels to the graph
plt.legend({'Mode':mode_value,'Mean':mean_value,'Median':median_value})

#relplot for variablity measure
# #sns.relplot(y=data['Positive'],x=data['Positive'])
ax_box.set_title('Test score')
ax_box.set(xlabel='')
ax_box.set(ylabel='')

plt.grid(which='major', alpha=0.5)
plt.show()