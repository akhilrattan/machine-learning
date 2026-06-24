import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

monthly_revenue = df.groupby("Month")["Total Amount"].sum()

plt.figure(figsize = (8,5))

plt.plot(monthly_revenue.index.astype(str),
         monthly_revenue.values,
         marker='o',
         label='Revenue')
plt.title("monthly revenue")
plt.xlabel("month")
plt.ylabel("revenue")
plt.legend()
plt.grid(True)
plt.show()

filter_products = df[df["Product Category"].isin(["Electronics","Clothing"])]

category_revenue = filter_products.groupby("Product Category")["Total Amount"].sum()

plt.figure(figsize=(8,5)) 
plt.bar(category_revenue.index,
        category_revenue.values,
        label='Revenue')
plt.title("product category vs total revenvue")
plt.xlabel("category")
plt.ylabel("revenue")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df['Quantity'],
         bins=15)
plt.title('Distribution of Quantity Ordered')
plt.xlabel('Quantity Ordered')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df['Price per Unit'],
            df['Total Amount'],
            alpha=0.1,
            label='Sales')

plt.title('Unit Price vs Revenue')
plt.xlabel('Unit Price')
plt.ylabel('Revenue')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
