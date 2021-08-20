import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string()) 

#Print rows and columns
print(df.describe) 

#Data Info
df.info()
