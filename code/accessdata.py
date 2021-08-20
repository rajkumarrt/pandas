import pandas as pd
data = {'Country' : ['UK', 'India', 'Australia', 'USA', 'France', 'UAE' ],
        'Cities': ['London', 'Chennai', 'Melbourne', 'Newyork', 'Parris', 'Dubai'],
        'Population': [99,89,78,79,67,72]}
datas = pd.DataFrame(data)

print((datas))

#Access data from a Pandas DataFrame
#Top 3 rows
print(datas.head(3))

#Bottom 3 Rows
print(datas.tail(3))

#print particular column data
print(datas['Country'])

#The iloc method gives us access to the DataFrame in more traditional ‘matrix’ style notation, i.e. [row, column] notation
datas.iloc[1,1]
