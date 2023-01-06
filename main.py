import pandas as pd
import numpy as np
import time

datasets = pd.read_csv("data/result.csv")

X = datasets.iloc[:, [3, 4, 5, 6, 7, 8]].values
Y = datasets.iloc[:, 9].values

i = 0
while i < len(X):
    X[i][0] = time.mktime(time.strptime(X[i][0], '%Y-%m-%d %H:%M:%S'))
    #print(X[i][0])
    i += 1

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.25, random_state = 42)

# Fitting Random Forest Regression to the Training set
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 40, random_state = 0)

regressor.fit(X_Train, Y_Train)

# Predicting the Test set results
y_pred = regressor.predict(X_Test)

print(y_pred)

# Evaluating the Algorithm
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_Test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(Y_Test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_Test, y_pred)))

