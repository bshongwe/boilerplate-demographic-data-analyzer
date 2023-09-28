import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('demographic_data.csv')

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  average_age_men = df[df['gender'] == 'Male']['age'].mean()

  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  higher_education_rich = round((higher_education['salary'] > 50000).mean() * 100, 1)

  # What percentage of people without advanced education make more than 50K?
  lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  lower_education_rich = round((lower_education['salary'] > 50000).mean() * 100, 1)

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  # percentage with salary >50K
  higher_education_rich = round((higher_education['salary'] > 50000).mean() * 100, 1)
  lower_education_rich = round((lower_education['salary'] > 50000).mean() * 100, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours_per_week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = df[df['hours_per_week'] == min_work_hours]
  rich_percentage = round((num_min_workers['salary'] > 50000).mean() * 100, 1)

  # What country has the highest percentage of people that earn >50K?
  country_groups = df.groupby('country')
  highest_earning_country = country_groups['salary'].mean().idxmax()
  highest_earning_country_percentage = round(country_groups['salary'].mean().max() * 100, 1)

  # Identify the most popular occupation for those who earn >50K in India

  # Filter the DataFrame to only include people who earn >50K in India
  df_filtered = df[(df['salary'] > 50000) & (df['country'] == 'India')]

  # Calculate the most common occupation
  top_IN_occupation = df_filtered['occupation'].mode()[0]

