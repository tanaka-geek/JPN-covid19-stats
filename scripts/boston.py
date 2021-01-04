
#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

import common.feature_selection as feat_sel
import common.test_env as test_env

boston = load_boston()

#give overall description and overview of the dataset
print(boston.keys())
print(boston.DESCR)
bostondf = pd.DataFrame(boston.data, columns=boston.feature_names)
bostondf['MEDV'] = boston.target

# check for missing values in all the columns
print("[INFO] dataset isnull():\n {}".format(bostondf.isnull().sum()))

# remove MEDV outliers (MEDV = 50.0)
bostondf = bostondf[~(bostondf['MEDV'] >= 50.0)]
print(np.shape(bostondf))