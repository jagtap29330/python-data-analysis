
import pandas as pd

# Sample sales dataset
data = {
    "order_id": [1, 2, 3, 4, 5],
    "product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
    "category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "quantity": [1, 2, 1, 1, 3],
    "price": [60000, 500, 800, 60000, 500]
}

df = pd.DataFrame(data)

# Create sales amount
df["sales_amount"] = df["quantity"] * df["price"]

df


# In[ ]:


# Total sales by category
category_sales = df.groupby("category")["sales_amount"].sum().reset_index()
category_sales


# In[ ]:


# Top selling products
product_sales = df.groupby("product")["sales_amount"].sum().sort_values(ascending=False)
product_sales


# In[ ]:


print("Key Insights:")
print("- Electronics generate the highest revenue")
print("- Laptops are the top revenue-contributing product")
print("- Accessories sell higher quantity but lower revenue")

