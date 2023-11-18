import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data_analysis_python_fcc/Medical Data Visualizer/medical_examination.csv')

bmi = df['weight'] / ((df['height'] / 100) ** 2)
overweight = []
for i in bmi:
    if i > 25:
        overweight.append(1)
    if i <= 25:
        overweight.append(0)
df['overweight'] = overweight
df_cat = df.melt(id_vars='cardio',
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
                     value_name='value')
df_cat = pd.DataFrame({'total':df_cat.groupby(['cardio', 'variable'])['value'].value_counts()})\
                                     .rename(columns={'cardio':'Cardio','variable':'Variable', 'value':'Value'})\
                                     .reset_index()
print(df_cat)