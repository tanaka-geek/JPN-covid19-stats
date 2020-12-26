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


# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.plot(df.index.values,
        df['Fatal'],
        linestyle="--",
        color='red',
        label="Death Toll",
        )

# Set title and labels for axes
# ax.set(xlabel="Date",
#        ylabel="",
#        title="",
#        label="Death Toll")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)


# df = sns.load_dataset('../covid_jpn_total.csv')
sns.lineplot(df.index.values, df['Active_Case'], ci='sd', data=df, label="Active Cases")
# sns.distplot(df['Fatal'], label="Fatal", bins=30,kde=False)
# sns.set(style='dark')

plt.title('Total Covid-19 Cases in Japan')
plt.xlabel("Date")
plt.ylabel("Active Cases")

# 線が足されるので、良い
plt.grid()
fig.tight_layout()
plt.show()

# fig, ax = plt.subplots(figsize=(10,10))

# #Add x-axis and y-axis
# ax.plot(df.index.values,
#         df['Active_Case'])

# # Set title and lables for axes
# ax.set(xlabel="Date",
#        ylabel="Positive Case",
#        title="Covid-19 Cases")

# plt.show()


# print(df.head())