# -*- coding: utf-8 -*-
"""movie_prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_MDmeQzThYEJyzgSdc4anUD7oZz420uu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv('/content/drive/MyDrive/Assignment/IMDb Movies India.csv',encoding='latin-1')

data.dropna(inplace=True)

data.head()

data.shape

import missingno
missingno.matrix(data)

data.describe()

data.isnull().sum().sum()   # there is no null value

# visualizing overall rating users

data['Rating'].value_counts().plot(kind='bar', alpha=0.7, figsize=(25,25))
plt.show()

# highest rating s

data['Duration'].value_counts().plot(kind='bar',  alpha=0.9, figsize=(38, 38))
plt.show()

duration = []
for d in data.Duration:
    if type(d) == float:
        duration.append(np.nan)
    else:
        duration.append(int(str(d).split(" ")[0]))
data["Duration"] = duration
data.head()

# histogram

data. Rating.plot.hist(bins=15)
plt.title('Distribution of rating')
plt.ylabel('count of users')
plt.xlabel('rating')

data["Votes"] = pd.to_numeric(data['Votes'].str.replace(',',''))
data.head()

genre_counts = {}
for genre in genre.values.flatten():
    if genre is not None:
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

genereCounts = {genre: count for genre, count in sorted(genre_counts.items())}
for genre, count in genereCounts.items():
    print(f"{genre}: {count}")

year = []
for y in data.Year:
    if type(y) == float:
        year.append(np.nan)
    else:
        year.append(int(str(y)[1:5]))
data["Year"] = year
data.head()



data.info()

data.describe()

data.isnull().sum().sum()

data.columns.values

import warnings
 warnings.filterwarnings('ignore')

data.shape

# camparison votes and genres that are related with Ratings

vgr = sns.pairplot(data, x_vars=['Votes', 'Genre'], y_vars='Rating', aspect=1, kind='scatter',)

sns.set_style('darkgrid')
d = data.loc[(data['Rating']>8) & (data['Votes']>10000), ['Rating','Votes','Name']]
plt.figure(figsize=(15, 6))
ax=sns.barplot(data=d,x='Name',y='Votes',hue='Rating',dodge=False,width=0.5,palette='muted')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
ax.legend(loc='upper right')
ax.set_xlabel('Movie Name')
ax.set_ylabel('Votes')
ax.set_title('Movies with rating greater than 8 and votes greater than 10000')
plt.show()


# top movies with raint greater than 8 and also more
#than 10000 votes so we can say that these movies are actually good.

sns.set_style('ticks')
plt.figure(figsize=(10, 6))
sns.lineplot(data=data,x='Year',y='Duration',errorbar=None)
plt.xlabel('Year')
plt.ylabel('Duration in minutes')
plt.title('Duration of movies by year')
plt.xticks(np.arange(1922,2023,5))
plt.show()

genre = data['Genre']
genre_stack = genre.str.split(',').apply(pd.Series).stack()
genre_stack.index = genre_stack.index.droplevel(-1)
g=[genre.str.split(',').apply(pd.Series)[i].str.strip().value_counts(dropna=False).to_dict() for i in range(3)]

g_dict = {k: sum(dic.get(k,0) for dic in g) for dic in g for k in dic}
genres_count = pd.Series(g_dict).sort_values(ascending=False).drop(np.nan)

genre_rating = {k:data.loc[data['Genre'].str.contains(k),'Rating'].mean().round(1) for k in genres_count.index}
genre_rating = pd.Series(genre_rating).sort_values(ascending=False)
genres_single = pd.concat([genres_count,genre_rating],axis=1).sort_values(by=1,ascending=False).rename(columns={0:'Movie count',1:'Average rating'})
genres_single.sort_values(by='Movie count',ascending=False,inplace=True)

sns.set_style('darkgrid')
plt.figure(figsize=(15,5))
sns.barplot(data=genres_single,x=genres_single.index.values,y='Movie count',palette='coolwarm')
plt.xlabel('Genre')
plt.ylabel('Number of movies')
plt.title('Number of movies in each genre')
plt.xticks(rotation=90)
plt.show()

sns.set_style('darkgrid')
plt.figure(figsize=(15,5))
sns.barplot(data=genres_single,x=genres_single.index.values,y='Average rating',palette='coolwarm')
plt.xlabel('Genre')
plt.ylabel('Average Rating')
plt.title('Average rating of movies in each genre')
plt.xticks(rotation=90)
plt.show()

# Now below Graph shows the average rating for each genre but drama
#has more movies so it is logical for rating to drop as some movies may have performed bad

genre_data = data.groupby('Genre').agg({'Rating':['mean','count']})
genre_data .reset_index(inplace=True)
genre_data .columns = ['Genre','Average Rating','Movie Count']
genre_data ['Average Rating'] = genre_data['Average Rating'].round(1)
genre_data

#For prediction of rating I will replace every genre with its average rating
# for all the movies for that particular genres and I will do same for directors and actors

# model building

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score as score

corr_df = data.corr(numeric_only=True)
corr_df['Rating'].sort_values(ascending=False)

Input = data.drop(['Name', 'Genre', 'Rating', 'Director', 'Actor 1', 'Actor 2', 'Actor 3'], axis=1)
Output = data['Rating']

Input.head(5)

Output.head(5)

def evaluate_model(y_true, y_pred, model_name):
    print("Model: ", model_name)
    print("Accuracy = {:0.2f}%".format(score(y_true, y_pred)*100))
    print("Mean Squared Error = {:0.2f}\n".format(mean_squared_error(y_true, y_pred, squared=False)))
    return round(score(y_true, y_pred)*100, 2)

x_train, x_test, y_train, y_test = train_test_split(Input, Output, test_size = 0.2, random_state = 1)

LR = LinearRegression()
LR.fit(x_train, y_train)
lr_preds = LR.predict(x_test)

LRScore = evaluate_model(y_test, lr_preds, "LINEAR REGRESSION")



















