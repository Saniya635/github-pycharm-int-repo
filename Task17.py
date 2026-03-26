#lab assignment 1
import pandas as pd
data = {
 'cut':['Ideal','Premium','Good','Premium','Good'],
 'price':[326,326,327,334,335],
 'x':[3.95,3.89,4.05,4.20,4.34],
 'y':[3.98,3.84,4.07,4.23,4.35],
 'z':[2.43,2.31,2.31,2.63,2.75]
}
df = pd.DataFrame(data)
print("Mean price:")
print(df.groupby('cut')['price'].mean())
print("\nMin price:")
print(df.groupby('cut')['price'].min())
print("\nMax price:")
print(df.groupby('cut')['price'].max())
print("\nAverage values:")
print(df[['x','y','z']].mean())

#lab assignment 2
import pandas as pd
data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Employee_Name': ['Amit', 'Neha', 'Raj', 'Simran', 'Karan'],
    'Department': ['Automotive', 'IT', 'Automotive', 'HR', 'Automotive'],
    'Designation': ['Manager', 'Developer', 'Engineer', 'Developer', 'Developer']
}
df = pd.DataFrame(data)
df.to_excel("employee.xlsx", index=False)
df = pd.read_excel("employee.xlsx")
print("Complete Data:\n", df)
print("\nEmployees in Automotive Department:")
print(df[df['Department'] == 'Automotive'])
emp_id = int(input("\nEnter Employee ID: "))
print(df[df['Employee_ID'] == emp_id])
print("\nList of Developers:")
print(df[df['Designation'] == 'Developer'])