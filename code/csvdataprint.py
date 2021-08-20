import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string()) 

#Print rows and columns
print(df.describe) 

#Data Info
df.info()

#Print columns Name
df.columns

#Print null values and count
df.isnull().sum()


#On an entire DataFrame we can get a summary of the distribution of continuous variables:
df.describe()

#Particular Column
df['Pulse'].describe()
