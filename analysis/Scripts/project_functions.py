##Imported modules
import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt

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
