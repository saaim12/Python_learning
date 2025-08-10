import numpy as np
import pandas as pd
# Creating a data dictionary
data_dict = {'A':[1,2,np.nan,4,np.nan],
            'B':[np.nan,np.nan,np.nan,np.nan,np.nan],
            'C':[11,12,13,14,15],
            'D':[16,np.nan,18,19,20]}
# Creating DataFrame form data_dict
df = pd.DataFrame(data_dict) # DataFrame from a dic.
df.index.name="index"
print(df)
print(df.isnull())
#For sum(), pandas considers NaN as 0
print(df['A'].sum())
df['new']=df['A'] + df ['D'] # inf any column have nan other one wil be nan
print(df)
# The methods dropna() and fillna() are helpful methods to clean and fill the missing data.
# The dropna() method drops any row (default value) that has a NaN value. Its default axis (row) is 0.
# The thresh parameter of this method is very useful. This parameter is of an int type and its default value is None.
# If we pass the parameter thresh = 3, the method will drop any column that has less than 3 non-NaN values.
print("Dropping Columns \n", df.dropna(axis=1))
# Calling the method with thresh
print("Threshed output \n ",df.dropna(thresh=3, axis=1))
# to fill the values
print("Filled DataFrame \n",df.fillna(value='Filled'))
# filling the values using mean value of column
print(df['A'].fillna(value = df['A'].mean()))
# filling with own values
# fill with your own given value
print(df.fillna(0))
print(df)