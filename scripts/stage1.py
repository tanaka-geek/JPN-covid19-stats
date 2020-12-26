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

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)

# Create another lineplot for active cases
sns.lineplot(df.index.values, df['Active_Case'], ci='sd', data=df, label="Active Cases")

# Add labels on side
plt.title('Total Covid-19 Cases in Japan')
plt.xlabel("Date")
plt.ylabel("Active Cases")

# 線が足されるので、良い
plt.grid()
fig.tight_layout()
plt.show()
