##Imported modules
import pandas as pd
import numpy as np
import seaborn as sns
import os 
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
#from .. import project_functions - invalid syntax

%matplotlib inline

from .. import project_functions # This is called a relative import
df = project_functions.load_and_process('heart_attack_processed.csv')
df

# Method chain 1 (Load data, clean data and deal with missing data)

heart_file = (data.rename(columns = {'age':'Age', 'sex':'Sex of Patient',
                     'cp':'Chest Pain','trtbps':'Resting bp(mmHg)','chol':'Cholesterol',
                     'restecg':'Resting ECG','thalachh':'Max Heart Rate','fbs':'Fasting Blood Sugar','output':'Result'})
        .dropna(axis ='columns')
        .sort_values("Cholesterol", ascending=True))


heart_file

#removed NaN values in columns
#renamed columns
# Cholesterol now in ascending values

## EDA
df = pd.read_csv("new_heart_file.csv")
df.shape
df.head()
df.columns

df.nunique(axis=0)
df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))

##Changed Result from 1 and 0 to yes and no
# Result yes = heart attack
df['Result']= df['Result'].map({1:'yes', 0:'no'}) 

df.groupby(by='Sex').size()
#this separates out the men and the women. Showing that there are more men in this study than women
# 0 = female
# 1 = male



ax = sns.histplot (data = df, x="Sex",stat="count")
ax.set_title ("Number of People by Sex")
# Figure showing that there were obviously more men in this study



sns.catplot(x="Result", data=df, kind="count", hue="Sex")
#Plot showing that men were more likely to have a heart attack in this sample dataset,than women

# Yes= heart attack
# No= No heart attack

#sns.catplot(x="Result", y="Age", data=df, kind="box")

sns.boxplot(x="Result", y="Age", data=df, hue="Sex",palette = "Set2")
#Boxplot showing the ages of patients against their result of a heart attack or not
