import pandas as pd
import re

path_customer = "/Users/harshitg/Documents/Per Fold/Assignments/customer_data.csv"
path_order = "/Users/harshitg/Documents/Per Fold/Assignments/Order.csv"

def load_customer_csv(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip().str.lower()
    return df

df1 = load_customer_csv(path_customer)
df2 = load_customer_csv(path_order)
##print(df.head())

#step1:  Check for special characters in name 
def check_special_chars(df):
    # Regex: anything NOT an alphabet
    pattern = re.compile(r'[^A-Za-z]')
    mask = (
            df['first'].astype(str).str.contains(pattern, na=False) |
            df['last'].astype(str).str.contains(pattern, na=False)
            )
    issues = df[mask]
    if issues.empty:
        print("No special characters found here")
    else:
        print("Records with special chrc")
        print(issues)
    return issues


#special_char_issues = check_special_chars(df1)


def check_null(df):
    """Flags records where any mandatory field is NULL"""
    mandatory_fields = ['customer_id', 'first', 'age', 'country']

    mask = df[mandatory_fields].isnull().any(axis=1)

    issues = df[mask]

    if issues.empty:
        print("No NULL values found in mandatory fields.")
    else:
        print("Records with NULL values in mandatory fields:")
        print(issues)

    return issues

null_char_issues = check_null(df1)


