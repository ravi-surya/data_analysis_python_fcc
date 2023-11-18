import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


    # Read data from file
df=pd.read_csv('data_analysis_python_fcc/Sea-Level-Predictor/epa-sea-level.csv')

    # Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_axis = np.arange(df['Year'].min(),2050,1)
print(x_axis)
y_axis = x_axis*line.slope + line.intercept
plt.plot(x_axis,y_axis)