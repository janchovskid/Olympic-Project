## -*- coding: utf-8 -*-
"""
Created on Mon January 9 18:14:57 2022

@author: draganjanchovski
"""

import statistics as stats
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv('C:\\Users\\burov\\Desktop\\All Year Olympic Dataset (with 2020 Tokyo Olympics).csv')

df.head()
df.tail(10)
df.ndim
df.shape
df.size
df.columns
df.index
df.info()
b=df.describe()
a=df.isna()
df.isna().sum()
df.corr()

from io import StringIO
output = StringIO()
df.info(buf=output)
data=output.getvalue().split('\n')
data=output.getvalue()

values={}
for column in df.columns:
    values[column]=dict(df[column].value_counts())

# Dropping the "Unnamed" column because we don't need it

df.drop(columns=['Unnamed: 0'],inplace=True)

# Dropping the missing values

df.dropna(inplace=True)

# Top 10 countries participating

top_10_countries = df.Team.value_counts().head(10)
top_10_countries
plt.figure(figsize=(12,6))
plt.title('Overall Participation by Country')
sns.barplot(x=top_10_countries.index, y=top_10_countries);

# Age distribution of the participants

plt.figure(figsize=(12,6))
plt.title('Age distribution of the participants')
plt.xlabel('Age')
plt.ylabel('Number of patricipants')
plt.hist(df.Age, bins = np.arange(10,80,2), color = 'orange', edgecolor = 'white');

# Winter Sports

winter_sports = df[df.Season == 'Winter'].Sport.unique()
winter_sports

# Summer Sports

summer_sports = df[df.Season == 'Summer'].Sport.unique()
summer_sports

# Male and Female participants

gender_counts = df.Sex.value_counts()
gender_counts
plt.figure(figsize=(12,6))
plt.title('Gender Distribution')
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=180, shadow=True);

# Women Participation

female_participants = df[df.Sex == 'F']
sns.set(style='darkgrid')
plt.figure(figsize=(20,10))
sns.countplot(x='Year', data=female_participants, palette='Spectral')
plt.title('Women Participation')

# Female Athletes over time

part = female_participants.groupby('Year')["Sex"].value_counts()
plt.figure(figsize=(20,10))
part.loc[:,'F'].plot()
plt.title('Plot of Female Athletes over time')

# Total medals

df.Medal.value_counts()
total_medals = df[(df.Medal > 0)]
total_medals.head(10)

# Gold medal athletes

gold_medals = df[(df.Medal == 3)]
gold_medals.head()

# Silver medal athletes

silver_medals = df[(df.Medal == 2)]
silver_medals.head()

# Bronze medal athletes

bronze_medals = df[(df.Medal == 1)]
bronze_medals.head()

# Gold medals beyond 60

gold_medals_over_60 = gold_medals["Name"][gold_medals['Age']>60]
gold_medals_over_60
plt.figure(figsize=(18,9))
plt.tight_layout()
sns.countplot(gold_medals_over_60)
plt.title('Gold medals for Athletes over 60')

# Medals from each country

total_medals_by_country = total_medals.Team.value_counts().reset_index(name='Medal').head(5)
a = sns.catplot(x='index', y='Medal', data=total_medals_by_country, height=7, kind='bar', palette='rocket')
a.despine(left=True)
a.set_xlabels('Top 5 countries')
a.set_ylabels('Number of medals')
plt.title('Medals per country')

# Gold medals from each country

total_gold_medals = gold_medals.Team.value_counts().reset_index(name='Medal').head(5)
a = sns.catplot(x='index', y='Medal', data=total_gold_medals, height=7, kind='bar', palette='rocket')
a.despine(left=True)
a.set_xlabels('Top 5 countries')
a.set_ylabels('Number of medals')
plt.title('Gold medals per country')

# Silver medals from each country

total_silver_medals = silver_medals.Team.value_counts().reset_index(name='Medal').head(5)
a = sns.catplot(x='index', y='Medal', data=total_silver_medals, height=7, kind='bar', palette='rocket')
a.despine(left=True)
a.set_xlabels('Top 5 countries')
a.set_ylabels('Number of medals')
plt.title('Silver medals per country')

# Bronze medals from each country

total_bronze_medals = bronze_medals.Team.value_counts().reset_index(name='Medal').head(5)
a = sns.catplot(x='index', y='Medal', data=total_bronze_medals, height=7, kind='bar', palette='rocket')
a.despine(left=True)
a.set_xlabels('Top 5 countries')
a.set_ylabels('Number of medals')
plt.title('Bronze medals per country')

# Medals by participants

medals_by_participants = df[(df.Medal > 0)].Name
sns.barplot(x=medals_by_participants.value_counts().head(20), y=medals_by_participants.value_counts().head(20).index)
plt.ylabel(None);
plt.xlabel('Medals by Participants');

# Gold medals by participants

gold_medals_by_participants = df[(df.Medal == 3)].Name
sns.barplot(x=gold_medals_by_participants.value_counts().head(20), y=gold_medals_by_participants.value_counts().head(20).index)
plt.ylabel(None);
plt.xlabel('Gold Medals by Participants');

# Silver medals by participants

silver_medals_by_participants = df[(df.Medal == 2)].Name
sns.barplot(x=silver_medals_by_participants.value_counts().head(20), y=silver_medals_by_participants.value_counts().head(20).index)
plt.ylabel(None);
plt.xlabel('Silver Medals by Participants');

# Bronze medals by participants

bronze_medals_by_participants = df[(df.Medal == 1)].Name
sns.barplot(x=bronze_medals_by_participants.value_counts().head(20), y=bronze_medals_by_participants.value_counts().head(20).index)
plt.ylabel(None);
plt.xlabel('Bronze Medals by Participants');

# Medals by age

medals_by_age = total_medals.Age.value_counts().reset_index(name='Medal').head(10)
a = sns.catplot(x='index', y='Medal', data=medals_by_age, height=7, kind='bar', palette='rocket')
a.despine(left=True)
a.set_xlabels('Age')
a.set_ylabels('Number of medals')
plt.title('Medals by age')

# Gold medals by age

gold_medals_by_age = gold_medals.Age.value_counts().reset_index(name='Medal').head(10)
a = sns.catplot(x='index', y='Medal', data=gold_medals_by_age, height=7, kind='bar', palette='rocket')
a.despine(left=True)
a.set_xlabels('Age')
a.set_ylabels('Number of medals')
plt.title('Gold medals by age')

# Silver medals by age

silver_medals_by_age = silver_medals.Age.value_counts().reset_index(name='Medal').head(10)
a = sns.catplot(x='index', y='Medal', data=silver_medals_by_age, height=7, kind='bar', palette='rocket')
a.despine(left=True)
a.set_xlabels('Age')
a.set_ylabels('Number of medals')
plt.title('Silver medals by age')

# Bronze medals by age

bronze_medals_by_age = bronze_medals.Age.value_counts().reset_index(name='Medal').head(10)
a = sns.catplot(x='index', y='Medal', data=bronze_medals_by_age, height=7, kind='bar', palette='rocket')
a.despine(left=True)
a.set_xlabels('Age')
a.set_ylabels('Number of medals')
plt.title('Bronze medals by age')

# Tokyo olympics

max_year = df.Year.max()
team_names = df[(df.Year == max_year) & (df.Medal == 3)].Team
team_names.value_counts().head(10)
sns.barplot(x=team_names.value_counts().head(20), y=team_names.value_counts().head(20).index)
plt.ylabel(None);
plt.xlabel('Countrywise Gold Medals for Tokyo olympcis');