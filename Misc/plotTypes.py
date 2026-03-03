import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Fruit': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Banana'],
    'Quantity': [10, 15, 7, 12, 9, 5, 14, 6]
}

df = pd.DataFrame(data)

#countplot/barplot
sns.countplot(x='Fruit', data=df)
plt.title("Count of Each Fruit")
plt.show()

# quantity_sum = df.groupby('Fruit')['Quantity'].sum().reset_index()
# #barplot
# sns.barplot(x='Fruit', y='Quantity', data=quantity_sum)
# plt.title("Total Quantity by Fruit Type")
# plt.show()
# #boxplot
# sns.boxplot(x='Fruit', y='Quantity', data=df)
# plt.title("Box Plot: Quantity Distribution by Fruit Type")
# plt.show()
# #violinplot
# sns.violinplot(x='Fruit', y='Quantity', data=df)
# plt.title("Violin Plot: Quantity Distribution by Fruit Type")
# plt.show()
