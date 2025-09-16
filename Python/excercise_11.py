# Exercise 1: Create a pandas DataFrame from a dictionary with the following data:
import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24,27,22] , 'City':['New york', 'London', 'Paris']})
# print(df)

# Excercise 2: Read a CSV file named students.csv into a pandas DataFrame.
# df = pd.read_csv('students.csv')
# print(df)

# Exercise 3: Display the first 3 rows, column names, and data types.
# df = pd.read_csv('C:\Cdac\students.csv')
# print(df.iloc[0:2,0:2])

# print(type(df))

# Exercise 4: Select only the Age column.
# print(df['Age'])

# Excercise 5: Filter Rows Select students whose age is greater than 23.
# k = df[df['Age']>23][['Name','City']]
# print(k)

# Exercise 6: Add a New Column Add a column Marks = [85, 90, 78] to the DataFrame.
# df['Marks'] = [85,90,78]
# print(df)

# Excercise 7: Summary Statistics Find the mean, min, and max of the Age column.
# import statistics

# print(statistics.mean(df['Age']))
# print(min(df['Age']))
# print(max(df['Age']))

#Excercise 8: Sort Data Sort the DataFrame by Marks in descending order.[Hint: use sort_values()]
# print(sorted(df['Marks']))

# Exercise 9: Group By Group the data by City and find the average Age.`
# k = df.groupby('City')['Age'].mean()
# print(k)

# Excercise 10: Save to CSV Save the DataFrame to a file named output.csv.
# df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24,27,22] , 'City':['New york', 'London', 'Paris']})
# df.to_csv('output.csv')

#Excercise 11: SF Salaries Exercise 

#1
dj = pd.read_csv(r'C:\Cdac\Salaries.csv', low_memory=False)
# print(dj.head())

#2. 
# dj.info()

#3.What is the average BasePay ? 

# dj['BasePay'] = pd.to_numeric(dj['BasePay'] , errors = 'coerce')
# print(dj['BasePay'].mean())

# 4. **What is the highest amount of OvertimePay in the dataset ? **
# print(max(pd.to_numeric(dj['OvertimePay'], errors = 'coerce')))

# 6** What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# position = dj['EmployeeName'] == 'JOSEPH DRISCOLL'
# title = dj.loc[position, 'JobTitle']
# print(title)


# 7** How much does JOSEPH DRISCOLL make (including benefits)? **
# i = dj['EmployeeName'] == 'JOSEPH DRISCOLL'
# total_pay = dj.loc[i, 'TotalPayBenefits']
# print(total_pay)


# 8** What is the name of highest paid person (including benefits)?**
# i = dj['TotalPayBenefits'] == max(dj['TotalPayBenefits'])
# heighest_pay = dj.loc[i, 'EmployeeName']
# print(heighest_pay)


# 9** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**
# i = dj['TotalPayBenefits'] == min(dj['TotalPayBenefits'])
# lowest_pay = dj.loc[i, 'EmployeeName']
# print(lowest_pay)

# 10** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
# dj['BasePay'] = pd.to_numeric(dj['BasePay'], errors = 'coerce')
# print(dj.groupby('Year')['BasePay'].mean())

# 11** How many unique job titles are there? **[Hint: Explore and use value_counts()
# k = dj['JobTitle'].nunique()
# print(k)

# 12** What are the top 5 most common jobs? **
# k = dj['JobTitle'].value_counts()
# print(k.head())


# 13** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **
# np = dj[dj['Year']==2013]
# count_title = np.groupby('JobTitle').size()
# unique_tite = count_title[count_title==1]
# print(len(unique_tite))










