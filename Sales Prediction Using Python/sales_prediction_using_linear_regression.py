# -*- coding: utf-8 -*-
"""sales_prediction_using_linear_regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e1wcHU27dmbgoVTyFhz18Nufon-M5c8s
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('/content/drive/MyDrive/Assignment/advertising (1).csv')

data

data.head()

data.info()

data.shape

data.describe()

# checking null

data.isnull().sum()

data.isnull().sum().sum()

sns.boxplot(data['Sales'])
plt.show()

sns.boxplot(data['Sales'])
plt.show()

# checing targer sales with other input variable (scatter plot)
sns.pairplot(data, x_vars=['TV', 'Newspaper', 'Radio'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()

data['TV'].plot.hist(bins=10, color="Magenta", title = 'Histogram of TV advertisements expences')

data['Radio'].plot.hist(bins=10, color = 'red', xlabel='Radio', title = 'Histogram Representation')

data['Newspaper'].plot.hist(bins=10, color = 'red', xlabel='Newspaper', title = 'Histogram Representation')

sns.heatmap(data.corr(), annot=True)
plt.show()

# here we are finding TV and sales have very high positive corr. between then as the corrr of tv and sales 0.9
# i.e. very close to the 1.

X = data['TV']
y = data['Sales']

print(X)

print(y)

from sklearn.model_selection import train_test_split  # 70 and 30
X_train, X_test, y_train, y_test = train_test_split(data[['TV']], data[['Sales']], test_size = 0.3, random_state=0)

X_train.head()

y_train.head()

X_train.shape   # test have 140 observation

X_test.shape     # testing have 60 observation

print(y_train)

print(X_test)

# model building

# Linear Regression

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# coefficient of model

model.coef_    # we will get index of the coefficient of the linear model.

# finding  intercept of the model -
0.05473199 * 69.2 + 9.88042193    #taking one predicted value



pred= model.predict(X_test)
print(pred)    # sales of the tv

# scatter of the test and predicted response corresponding to train data .

plt.scatter(X_test, y_test)
plt.plot(X_test, 7.54336581 + 0.05473199 * X_test, 'r')

# the residuals are completely random and does not follow.

