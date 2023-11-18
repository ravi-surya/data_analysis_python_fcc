import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv('data_analysis_python_fcc/Sea-Level-Predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_axis = np.arange(df['Year'].min(),2050,1)
    y_axis = x_axis*line.slope + line.intercept
    plt.plot(x_axis,y_axis)
    # Create second line of best fit
    df2 =df[df['Year']>=2000]

    line2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    x_axis2=np.arange(2000,2050,1)
    y_axis2=x_axis2*line2.slope +line2.intercept

    plt.plot(x_axis2,y_axis2)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.close()
    return plt.gca()