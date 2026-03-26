#lab assignment 1
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'month': ['Jan','Feb','Mar','Apr','May','Jun'],
    'facecream': [2500,2630,2140,3400,3600,2760],
    'facewash': [1500,1200,1340,1130,1740,1555],
    'toothpaste': [5200,5100,4550,5870,4560,4890],
    'bathingsoap': [9200,6100,9550,8870,7760,7490],
    'shampoo': [1200,2100,3550,1870,1560,1890],
    'moisturizer': [1500,1200,1340,1130,1740,1555],
    'total_profit': [211000,183300,224700,230000,190000,210000]
}
df = pd.DataFrame(data)
plt.plot(df['month'], df['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()
plt.plot(df['month'], df['facecream'])
plt.plot(df['month'], df['facewash'])
plt.plot(df['month'], df['toothpaste'])
plt.legend(['Face Cream','Face Wash','Toothpaste'])
plt.title("Product Sales Data")
plt.show()
plt.bar(df['month'], df['facecream'])
plt.bar(df['month'], df['facewash'], bottom=df['facecream'])
plt.title("Face Cream & Face Wash Sales")
plt.show()
yearly = df[['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']].sum()
plt.pie(yearly, labels=yearly.index, autopct='%1.1f%%')
plt.title("Yearly Product Sales")
plt.show()

#lab assignment 2
import matplotlib.pyplot as plt
companies = ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','Amdocs']
recruitments = [120,150,180,90,110,130,80]es, recruitments)
plt.title("Recruitments by Company")
plt.xticks(rotation=30)
plt.show()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Share")
plt.show()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        explode=[0,0.1,0,0,0,0,0])
plt.title("Customized Pie Chart")
plt.show()
plt.pie(recruitments, labels=companies)
circle = plt.Circle((0,0),0.5,color='white')
plt.gca().add_artist(circle)
plt.title("Doughnut Chart")
plt.show()