import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("C://Users/aksl8/Downloads/Orders.csv")

# Group data by 'City', 'Product Category', and 'Product' and count orders
city_category_product_count = data.groupby(['City', 'Product Category', 'Product']).size().reset_index(name='Order_count')

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Loop through each city and plot the counts for each product category and product
for city in city_category_product_count['City'].unique():
    city_data = city_category_product_count[city_category_product_count['City'] == city]
    categories = city_data['Product Category'].unique()

    for category in categories:
        category_data = city_data[city_data['Product Category'] == category]
        ax.barh(category_data['Product'], category_data['Order_count'], label=f"{city} - {category}")

# Add labels, title, and legend
ax.set_xlabel('Number of Orders')
ax.set_ylabel('Product')
ax.set_title('City-wise Orders by Product Category and Product')
ax.legend(title='City - Product Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()
