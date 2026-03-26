#lab assignment 1
import pandas as pd
data = {
    'Title':['Book1','Book2','Book3'],
    'Author':['A','B','A'],
    'Year':[2001,1999,2010],
    'Publisher':['P1','P2','P1'],
    'Price':[500,300,700]
}
df = pd.DataFrame(data)
print(df)
print("\nBooks by Author A:")
print(df[df['Author']=='A'])
print("\nBooks by Publisher P1:")
print(df[df['Publisher']=='P1'])
print("\nCheapest Book:")
print(df[df['Price']==df['Price'].min()])
print("\nCostliest Book:")
print(df[df['Price']==df['Price'].max()])
print("\nSorted by Year:")
print(df.sort_values(by='Year'))

#lab assignment 2
import pandas as pd
data = {
    'State':['A','B','C','D','E'],
    'Area':[1000,2000,1500,1800,2200],
    'Population':[50000,80000,60000,90000,75000]
}
df = pd.DataFrame(data)
print(df)
print("\nLargest Area State:")
print(df.loc[df['Area'].idxmax()])
print("\nLargest Population State:")
print(df.loc[df['Population'].idxmax()])
df['Density'] = df['Population'] / df['Area']
print("\nWith Density:")
print(df)
print("\nHighest Density State:")
print(df.loc[df['Density'].idxmax()])