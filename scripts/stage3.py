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
# Get the latest date data now it is 2020 Dec 23rd
df2 = df.loc[datetime.date(year=2020,month=12,day=23):datetime.date(year=2020,month=12,day=23)]

df3 = pd.read_csv('../jpn_geograph.csv')

# This is how you merge different dataframes based on the 'Prefecture'
nf = df2.merge(df3,left_on=('Prefecture'),right_on=('Prefecture'),how='inner',suffixes=('_left','_right'))
# nf = nf.drop(columns=['Hosp_require','Hosp_severe',
#  'Capital', 'Male','Female', 'Annual_Change',
#  'Est_Population','Discharged','Area'])


nf = nf.drop(columns=['Area','Annual_Change','Est_Population','Female','Male'])

def corrmatrix(df):
    corrMatrix = df.corr()
    sns.heatmap(corrMatrix, annot=True)
    plt.show()

def scatterplot(x, y):
    plt.scatter(x, y) # x and y as arguments
    plt.show()

scatterplot(nf['Positive'],nf['Tested'])

