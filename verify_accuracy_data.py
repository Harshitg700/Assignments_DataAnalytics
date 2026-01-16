import pandas as pd
import re

path_customer = "<PATH_TO_CUSTOMER_DATA>"
path_order = "<PATH_TO_ORDER_DATA>"
path_shipping = "<PATH_TO_SHIPPING_FILE>"

def load_customer_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df

df1 = load_customer_csv(path_customer)
df2 = load_customer_csv(path_order)
#print(df1.head())

df3 = pd.read_json(path_shipping)
#print(df3.head())

def check_special_chars(df,column_name):
    non_alpha_pattern = r'[^A-Za-z]'
    pattern = re.compile(non_alpha_pattern)
    mask = df[column_name].astype(str).str.contains(pattern, na=False)
    issues = df[mask]
    if issues.empty:
        print("No special characters found here")
    else:
        print("Records with special chrc")
        print(issues)
    return issues

def check_accuracy(df):
    special_chars_check_cols = ['First', 'Last', 'Age', 'Country'] 
    for col in special_chars_check_cols:
        check_special_chars(df, col)
    



# Accuracy checks
check_special_chars(df1,'First')
#check_special_chars(df1,'Last')
#check_special_chars(df2,'Item')
# check_special_chars(df3,'Status')
#check_accuracy(df1)

def check_nulls_or_zeroes(df, column_name):
    mask = df[column_name].isnull() | (df[column_name] == 0)
    issues = df[mask]

    if issues.empty:
        print(f"No NULL or ZERO values found in '{column_name}'")
    else:
        print(f"Records with NULL or ZERO in '{column_name}':")
        print(issues)

    return issues

##Completeness
#print(df1.head())
#check_nulls_or_zeroes(df1,'First')
# #check_null(df1,'first')
# print(df3.head())
# check_nulls(df3,'Shipping_ID')




