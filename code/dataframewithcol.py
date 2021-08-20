import pandas as pd
data = {'Country' : ['UK', 'India', 'Australia' ],
        'Cities': ['London', 'Chennai', 'Melbourne'],
        'Population': [99,89,78]}
datas = pd.DataFrame(data)

print((datas))

#Priniting Columnnames
for col in datas.columns:
    print(col)

#To List Columnnames  
datas.columns.tolist()

#Sorting Columnnames
sorted(datas)
