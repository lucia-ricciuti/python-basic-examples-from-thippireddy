import pandas as pd

customer_df = pd.read_csv('customer.csv') 
print(customer_df)

customer_df.to_csv('customer.csv')