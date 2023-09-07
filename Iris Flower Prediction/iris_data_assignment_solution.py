# -*- coding: utf-8 -*-
"""iris_data_assignment_solution

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wqclc66AtCCPVOm0kOKGdeVUJerpK-j-
"""



"""WorkFlow information

data set is 3 classes and 50 instances
here is 4 input and one output (species)
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns  # single line model

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv('/content/drive/MyDrive/Assignment/IRIS.csv')

data.head()

# displaying statsistical about data

data.describe()

data.info()

"""preprocessing

"""

data.isnull().sum().sum()

data['sepal_length'].hist()  # only one input

species_plot = data['species'].value_counts().plot.bar(title = 'IRIS FLOWER Distribution')
species_plot.set_xlabel('Class',size=20)
species_plot.set_ylabel('Count',size=20)

# all input in the histogram

# scatterplot

colors = ['red', 'yellow', 'green']
species = ['Iris-setosa',
    'Iris-versicolor',
    'iris-virginica']

for i in range(3):
  x = data[data['species'] == species[i]]
  plt.scatter(x['sepal_length'], x['sepal_width'], c = colors[i], label=species[i])

plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
plt.legend()

for i in range(3):
  x = data[data['species'] == species[i]]
  plt.scatter(x['petal_length'], x['petal_width'], c = colors[i], label=species[i])

plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.legend()

# coorelation matrix ---


data.corr

corr= data.corr()
fig, ax = plt.subplots(figsize=(15,15))
sns.heatmap(corr, annot=True, ax=ax)

# label encoding

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
# it is more importsnt part becausr it is converting the string to some numeric value of output column species

data['species'] = le.fit_transform(data['species'])
data.head()

#model training
from sklearn.model_selection import train_test_split
X = data.drop(columns=['species'])
Y = data['species']
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.30)

# logistic regression

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(x_train, y_train)

model.score(x_test, y_test)*100

# knn

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()

model.fit(x_train, y_train)

model.score(x_test, y_test)*100

# cross validation

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

l_model = LogisticRegression()

scores = cross_val_score(l_model, X, Y, cv=5, scoring='accuracy')

mean_accuracy=scores.mean()

mean_accuracy

