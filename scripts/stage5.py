import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime 
import calendar
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from meta import *
from statsmodels.nonparametric.smoothers_lowess import lowess

# Date now has become index
df = pd.read_csv('../datasets/covid_jpn_domestic_total.csv')

X = pd.DataFrame(np.c_[df.Positive], columns=['Infect Toll'])
Y = df.index.values

print(X.shape)
print(Y.shape)

#Training and Testing ratio 70% : 30%

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=5)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

lm = LinearRegression()
lm.fit(X_train, Y_train)

print('Linear Regression Coefficients: {}'.format(lm.coef_))
print('Linear Regression Intercept: {}'.format(lm.intercept_))

# Training dataset
y_train_predict = lm.predict(X_train)

# Regression Line <- Intercept & Slope
b, m = np.polynomial.polynomial.polyfit(Y_train, y_train_predict, 1)

# Scatterplot for Predicted Training Dataset
sns.scatterplot(Y_train, y_train_predict, alpha=0.3)
sns.regplot(Y_train, y_train_predict, truncate=True, scatter_kws={'s': 20, 'alpha':0.3}, line_kws={'color':'red', 'linewidth': 2})
sns.lineplot(np.unique(Y_train), np.unique(np.poly1d(b + m * np.unique(Y_train))), linewidth=0.5, color='b')

plt.xlabel("Days Passed (Days)")
plt.ylabel("Positive Cases (K)")
plt.title("Actual Cases vs Predicted Cases")
plt.show()

# Linear Model Performance
rmse = (np.sqrt(mean_squared_error(Y_train, y_train_predict)))
r2 = r2_score(Y_train, y_train_predict)
print("The linear model performance for training set")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))

# Model Evaluation
y_test_predict = lm.predict(X_test)

# Scatterplot for Predicted Training Dataset
sns.scatterplot(Y_test, y_test_predict, alpha=0.4)
sns.regplot(Y_test, y_test_predict, truncate=True, scatter_kws={'s': 20, 'alpha':0.3}, line_kws={'color':'green', 'linewidth': 1.5})

plt.xlabel("Days Passed (Days)")
plt.ylabel("Positive Cases (K)")
plt.title("Actual Cases vs Predicted Cases")
 
plt.show()

#Get the linear model performance for test set
# root mean square error of the model
rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))
# r-squared score of the model
r2 = r2_score(Y_test, y_test_predict)

#Defining MAPE function
def MAPE(Y_actual,Y_Predicted):
    mape = np.mean(np.abs((Y_actual - Y_Predicted)/Y_actual))*100
    return mape

print("\nThe linear model performance for testing set")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
LR_MAPE= MAPE(Y_test,y_test_predict)
print("MAPE: ",LR_MAPE)

y_train_residual = y_train_predict - Y_train
y_test_residual = y_test_predict - Y_test

plt.subplot(1, 2, 1)
sns.distplot(y_train_residual, bins=15)
plt.title('Residual Histogram for Training Set')

plt.subplot(1, 2, 2)
sns.distplot(y_test_residual, bins=15)
plt.title('Residual Histogram for Test Set')

plt.show()

fig, axes = plt.subplots()
fig.suptitle('Residual plot of Training and Test set')

# Plot the residuals after fitting a linear model
sns.residplot(y_train_predict, y_train_residual, lowess=True, color="b", ax=axes, label='Training Set', 
              scatter_kws={'s': 25, 'alpha':0.3})

sns.residplot(y_test_predict, y_test_residual, lowess=True, color="g", ax=axes, label='Test Set',
              scatter_kws={'s': 25})

legend = axes.legend(loc='upper left', shadow=True, fontsize='large')
legend.get_frame().set_facecolor('#f9e79f')

plt.xlabel('Predicted')
plt.ylabel('Residual')
plt.show()

#create some polynomial features
poly_features = PolynomialFeatures(degree=2)
# transform the features to higher degree features.
X_train_poly = poly_features.fit_transform(X_train)
# fit the transformed features to Linear Regression
poly_model = LinearRegression()
poly_model.fit(X_train_poly, Y_train)
     
# predicting on training data-set
y_train_predicted = poly_model.predict(X_train_poly)
# predicting on test data-set
y_test_predicted = poly_model.predict(poly_features.fit_transform(X_test))

y_train_residual = y_train_predicted - Y_train
y_test_residual = y_test_predicted - Y_test

plt.subplot(1, 2, 1)
sns.distplot(y_train_residual, bins=15)
plt.title('Residual Histogram for Training Set [Polynomial Model]')
plt.subplot(1, 2, 2)
sns.distplot(y_test_residual, bins=15)
plt.title('Residual Histogram for Test Set [Polynomial Model]')
plt.show()

sns.scatterplot(Y_train, y_train_predicted, alpha=0.4)
sns.regplot(Y_train, y_train_predicted, scatter_kws={'s': 20, 'alpha':0.3}, line_kws={'color':'green', 'linewidth': 2}, order=2)
 
plt.xlabel("Days Passed (Days)")
plt.ylabel("Positive Cases (K)")
plt.title("Actual Cases vs Predicted Cases")
 
plt.show()

sns.scatterplot(Y_test, y_test_predicted, alpha=0.4)
sns.regplot(Y_test, y_test_predicted, scatter_kws={'s': 20, 'alpha':0.3}, line_kws={'color':'green', 'linewidth': 2}, order=2)
 
plt.xlabel("Days Passed (Days)")
plt.ylabel("Positive Cases (K)")
plt.title("Actual Cases vs Predicted Cases")
 
plt.show()

# evaluating the model on training data-set
rmse_train = np.sqrt(mean_squared_error(Y_train, y_train_predicted))
r2_train = r2_score(Y_train, y_train_predicted)
     
print("The polynomial model performance for the training set")
print("RMSE of training set is {}".format(rmse_train))
print("R2 score of training set is {}".format(r2_train))

# evaluating the model on test data-set
rmse_test = np.sqrt(mean_squared_error(Y_test, y_test_predicted))
r2_test = r2_score(Y_test, y_test_predicted)

print("The polynomial model performance for the test set")
print("RMSE of test set is {}".format(rmse_test))
print("R2 score of test set is {}".format(r2_test))
PR_MAPE= MAPE(Y_test,y_test_predicted)
print("MAPE: ",PR_MAPE)
