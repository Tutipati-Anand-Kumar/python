import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C://Users/aksl8/Downloads/Orders.csv")
Orders_per_city =data.groupby('City').size().reset_index(name = 'Product_count')
print(Orders_per_city)
plt.bar(Orders_per_city['City'],Orders_per_city['Product_count'])
plt.xlabel('City')
plt.ylabel('Number of Products')
plt.title('Number of Products in Each City')
plt.show()