import pandas as pd
data = {'Country' : ['UK', 'India', 'Australia', 'USA', 'France', 'UAE' ],
        'Cities': ['London', 'Chennai', 'Melbourne', 'Newyork', 'Parris', 'Dubai'],
        'Population': [99,89,78,79,67,72]}
datas = pd.DataFrame(data)

#Boolean result
datas.Population > 80

# Data is true
datas[datas.Population > 80]
