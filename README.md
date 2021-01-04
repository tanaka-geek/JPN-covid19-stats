# statistics-probablity-project

## Stage 1 

### The topic of this data science project 

The dataset is obtained from [kaggle](https://www.kaggle.com/lisphilar/covid19-dataset-in-japan?select=covid_jpn_metadata.csv)

This is a covid-19 dataset in Japan. 
The dataset include the following.

- Total number of cases in Japan
- The number of cases at prefecture level
- Metadata of each prefecture

There are attributes for respective dataset.
The variables are the following.

- `Date` : YYYY-MM-DD 
- `Prefecture` : char  
- `Positive` : int
- `Tested` : int
- `Discharged` : int
- `Fatal` : int
- `Hosp_required` : int  
- `Hosp_severe` : int

Additionally, I have added one variable `Active_Case` to track the actual positive cases. 
`Active_Case` = `Positive` - `Discharged` 

There is no other missing data or errors (NA etc) in this dataset.

### Basic Distribution Graph 

![alt stage1.png](https://github.com/mr-wacker/statistics-probablity-project/blob/master/img/Stage1.png)


## Stage 2 

### Compute Central Tendency and Variability Measures

![alt stage2.png](https://github.com/mr-wacker/statistics-probablity-project/blob/master/img/Stage2.png)


In our dataset, the variable `Positive` of the latest date is picked.
As per boxplots/hisogram of this variable, the following factors are discovered.

- `Mode` : It is extremely higher (5.2k)and derivative scalar in the graph.
This is due to the fact that Tokyo has so much higher infection rate and population.

- `Median` : This was (161) in `Hyogo Prefecture`. 

- `Mean` : The average positive cases is (434.4) among 47 prefectures. This is higher than `Median` value '161'. It can be inferred that there are scalar values `Positive` with significant higher values which gives a skew to this `Mean` and `Median` values in comparison.

Central tendency

## Stage 3

Compute correlation matrix. 

![alt stage3.png](https://github.com/mr-wacker/statistics-probablity-project/blob/master/img/Stage3.png)

### Correlation Analysis

Correlated variables are the following

-  `Fatal` and `Hosp_require` 
-  `Positive` and `Population` 

`Fatal` and `Hosp_require` are correlated since the more people are in severe infected condition, the fatality cases are likely to increase.

`Positive` and `Population` are also correlated because the more population means higher probablity of infection. 

However, it is observable that `Hosp_severe` is only correlated with `Fatal` and shares lower correlation rate with other variables.

Presumably, Severe cases on covid-19 is due to the fact that although many population can be infected, only minority number of the infected experience severe cases because of variant factors such as their age, pre-medical condition and limited treatment in the hospital in country-side area.

Therefore, We can conclude that `Hosp_severe` is indepent variable except with `Fatal`.

We also conclude for dependent variable in this dataset is `Positive` and the rest are more or less dependent variables except `Hosp_severe`

# Stage 5

After multiple linear regression analysis, `Positive` is defined as dependent variable. 

However, straight regression line is not able to calculate the patterns which in the dataset is underfitting. In order to resolve this issue, the complexity of the model must be increased which the original features of the model are converted into the higher order polynomial terms. This operation is possible with the help of `scikit-learn` module.

The model is trained with 70-30 ratio.

According to the different types of regression models used for the analysis, the R-squared gets the value around 0.80~. This almost represents a model that explains all of the variation in the response variable around its mean.


Various analysis are conducted by using Linear and Polynomial Regression Models.
The x variable is `Positive` and `Date` (Dataframe Date's Index Values)
Caution for the `Date`, it is converted into the number of days passed. (Integer)

```
X = pd.DataFrame(np.c_[df.Positive], columns=['Infect Toll'])
Y = df.index.values
```

Linear Regression coefficient was calculated as `0.00162564`

RMSE, R2's value and MAPE are calculated respectively.

The Linear Model's performance for training:

- RMSE : 35.755953979357685
- R2 : 0.8491951960374975

The Linear Model's performance for testing:

- RMSE : 31.36388399092678
- R2 : 0.8816123287196085
- MAPE:  39.87470903917527

The Polynomial Model's performance for training:

- RMSE : 21.040343639302094
- R2 : 0.9477815358294585

The Polynomial Model's performatnce for testing: 

- RMSE :17.514006809561216
- R2 :0.9630837287177351
- MAPE: : 18.110589685632135
