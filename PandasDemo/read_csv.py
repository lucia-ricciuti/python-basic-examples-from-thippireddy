import pandas as pd

customer_df = pd.read_csv('customer.csv') 
print(customer_df)

customer_df = pd.read_csv(
    'customer_no_header.csv', 
    names=['first_name','last_name','email','phone']) 
print(customer_df)