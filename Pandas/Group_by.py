import pandas as pd
data = {'Store':['Walmart','Walmart','Costco','Costco','Target','Target'],
       'Customer':['Tim','Jermy','Mark','Denice','Ray','Sam'],
       'Sales':[150,200,550,90,430,120]}

df=pd.DataFrame(data=data,index=range(6))
print(df)
# Let's create new grouped DataFrame "by_store" after grouping on "store" column
by_store = df.groupby("Store")
print(" grouped by store\n",by_store)
print("===> mean \n",by_store['Sales'].mean())
# In one line of code using sum ad loc methods
print(df.groupby('Store',as_index=True).sum(numeric_only=True).loc["Target"])
print("\nMinimum value of sale \n", by_store.min()) # minimum value of sale
print("\nMaximum value of sale \n", by_store.max()) # maximum value of sale
print("\nStandard deviation of sale \n", by_store.std(numeric_only=True)) # standard deviation of sale
# Let's count the number of instances in each column, this operation works with strings as well
# we have 2 customers for each store and 2 sales for each store
print("\nCount : ", by_store.count())

# summary statistics using describe on grouped DataFrame
print(by_store.describe())
print()
# transpose after describe (two operations in one go!)
print(by_store.describe().transpose() )
print()
# summary statistics for Costco
print(by_store.describe().transpose()['Costco'])