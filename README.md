# statistics-probablity-project

## Stage 1 

### The topic of this data science project 

The dataset is obtained from [kaggle](https://www.kaggle.com/lisphilar/covid19-dataset-in-japan?select=covid_jpn_metadata.csv)

This is a covid-19 dataset in Japan. 
This does not include the cases in Diamond Princess cruise ship.

The variables are the following.
Except the first two are numerical values.

- Date : FORMAT YYYY-MM-DD 
- Prefecture : 47 prefectures 
- Positive : 
- Tested
- Discharged
- Fatal
- Hosp_required : Needs to be taken to Hospital  
- Hosp_severe : Fatal at hospital

There is no missing data or errors (NA etc) in this dataset.

### Basic Distribution Graph 

![alt stage1.png](https://github.com/mr-wacker/statistics-probablity-project/blob/master/img/Stage1.png)


## Stage 2 

Compute Central Tendency and Variability Measures

Central tendency

## Stage 3

Compute correlation matrix. 

![alt stage1.png](https://github.com/mr-wacker/statistics-probablity-project/blob/master/img/Stage3.png)

### Correlation Analysis

Correlated variables are the following

-  `Fatal` and `Hosp_require` 
-  `Positive` and `Population` 

`Fatal` and `Hosp_require` are correlated since the more people are in severe infected condition, the fatality cases are likely to increase.

`Positive` and `Population` are also correlated because the more population means higher probablity of infection. 

However, it is observable that `Hosp_severe` is only correlated with `Fatal` and shares lower correlation rate with other variables.

Presumably, Severe cases on covid-19 is due to the fact that although many population can be infected, only minority number of the infected experience severe cases because of factors such as their age, pre-medical condition and limited treatment in the hospital.

Therefore, `Hosp_severe` is indepent variable except with `Fatal`.







