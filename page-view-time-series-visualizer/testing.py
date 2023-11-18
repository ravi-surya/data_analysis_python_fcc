import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar
register_matplotlib_converters()

df = pd.read_csv('data_analysis_python_fcc/boilerplate-page-view-time-series-visualizer/fcc-forum-pageviews.csv')
df['date']=df['date'].astype('datetime64[ns]')
df=df.set_index("date")

df_bar = df.copy()

df_bar['year']=df.index.year
df_bar['month']=df.index.month_name()
print(df_bar.head())
df_bar_group = df_bar.groupby(['year', 'month'])['value'].mean()

df_bar_group = df_bar_group.unstack(level='month')
print(df_bar_group.head())
df_bar_group = df_bar_group[['January', 'February', 'March', 'April', 'May',
                                'June', 'July', 'August', 'September', 'October', 'November', 'December']]
