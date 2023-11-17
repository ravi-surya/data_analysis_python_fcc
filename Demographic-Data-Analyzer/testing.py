
#RUBBISH FOLDER DONE FOR PRACTISING IGNORE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import pandas as pd
import demographic_data_analyzer

df = pd.read_csv('C:/Users/ravis/Desktop/freecodecamp/data_analysis_python_fcc/Demographic-Data-Analyzer/adult.data.csv')
df.head()
   # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df['race'].value_counts()

    # What is the average age of men?
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round(df[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
highered = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
all_50 = df['salary'] == '>50K'

higher_education_rich = round((highered & all_50).sum() / highered.sum() * 100, 1)
lower_education_rich = round((~highered & all_50).sum() / (~highered).sum() * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
q1 = df['hours-per-week'] == min_work_hours

rich_percentage = round((q1 & all_50).sum() / q1.sum() * 100, 1)

    # What country has the highest percentage of people that earn >50K?
p_series = (df[all_50]['native-country'].value_counts() /df['native-country'].value_counts() * 100).sort_values(ascending=False)

highest_earning_country = p_series.index[0]
highest_earning_country_percentage = round(p_series.iloc[0], 1)
print(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & all_50]['occupation'].value_counts().index[0]

print(top_IN_occupation)