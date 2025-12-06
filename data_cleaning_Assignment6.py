
"""
================================================================
EXTRACT, LOAD, TRANSFORM, INSPECT, AND SAVE DATA FROM A CSV FILE
================================================================


STEP 1
First,Extract and load into a pandas Dataframe"""
import pandas as pd
import numpy as np
data = pd.read_csv(r"C:\Users\LENOVO\Desktop\PYHON _ASSIGNMENTS\Assignment6\Assignment_6_raw_sales_data3.csv")
df = pd.DataFrame(data)
#Example 4: Bulk Rename with Function 

'''Standardize Columns (convert to snake case)'''
def clean_column_name(col): 
    return col.strip().lower().replace(' ', '_').replace('-', 
'_') 
df.columns = [clean_column_name(col) for col in df.columns] 
print("\nTHE COLUMNS")
print(df.columns)


'''STEP 2
INSPECT THE DATAFRAME'''

'''Check the first 5 rows'''
print("\nTHE HEAD")
print(df.head())

'''print the last 5 '''
print("\nTHE TAIL")
print(df.tail())

print("\nDESCRIBED")
print(df.describe())

print("\nSHAPE OF DATAFRAME")
print(df.shape)


'''the overview of the data'''
print("\nDATA OVERVIEW")
print(df.info())
print(df)


'''replace empty str with Nan'''
print("\nEMPTY STR REPLACED")
df.replace('', np.nan, inplace=True) 

'''CHECK FOR MISSING VALS'''
print("\nMISSING VAL COUNTS")
print(df.isnull().sum())


'''=================fill missing vals in age, quantity, and price with mean and median'''
df['age'] = df['age'].fillna(df['age'].median())
df['age'] = df['age'].astype(int)
df['price'] = df['price'].fillna(df['price'].mean()).round(2)

# Negative values were encounterd in "quantity and price so we convert it to NaN and fill with mean"
df.loc[df['quantity'] < 0, 'quantity'] = np.nan
df.loc[df['price'] < 0, 'price'] = np.nan

df['quantity'] = df['quantity'].fillna(df['quantity'].mean()).round(2)
df['price'] = df['price'].fillna(df['price'].mean()).round(2)


'''=========================drop row with invalid purchase date'''
# '''For purhase date, we first convert the purchase date to datetime so that non valid datetime will return NaT
# and be available for dropping'''
df['purchase_date'] = pd.to_datetime(df['purchase_date'], format='%Y-%m-%d', errors='coerce')

# Converts the Purchase_Date column to datetime format.
# *errors='coerce'*: Any invalid date formats (e.g. "Invalid" 
# or wrong format) are turned into NaT (Not a Time), making them easy to remove later.
# '''

'''Drop NaT'''
df = df.dropna(subset=['purchase_date'])


'''===========================Convert uknown to NaN and drop'''
df.replace('unknown', np.nan, inplace=True)
df.dropna(subset=['customer_name', 'email', 'gender'], inplace=True)


'''==========================Convert all words in the dataframe to pascal case'''
import re

def to_pascal_case(val):
    if isinstance(val, str):
        # Skip if it's an email (simple check for '@' presence)
        if '@' in val:
            return val
        # Convert to PascalCase
        words = re.split(r'\W+', val)
        return ''.join(word.capitalize() for word in words if word)
    return val

#Apply only to columns except 'email'
for col in df.columns:
    if col != 'email':
        df[col] = df[col].apply(to_pascal_case)

# - Imports the *re* module, Python’s built-in regular expressions library, used here to split text into words based on non-word characters.
# def to_pascal_case(val):
# - Defines a function to_pascal_case that takes a single value (val) as input.
#     if isinstance(val, str):
# - Checks if the value is a string. If not, it returns the value unchanged later.
#         if '@' in val:
#             return val
# - Checks if the string contains '@', a simple way to detect email addresses. If yes, it returns the value as-is without changing it.
#         words = re.split(r'\W+', val)
# - Uses regular expression to split the string into words by non-word characters (\W+ means one or more characters that are NOT letters, digits, or underscore). For example, "hello_world!" becomes ['hello', 'world'].
#         return ''.join(word.capitalize() for word in words if word)
# - Capitalizes the first letter of each word and joins them together without spaces to create PascalCase. For example, ["hello", "world"] becomes "HelloWorld".
# - The if word part skips empty strings that may occur from splitting.

'''==================Rset index'''
df.reset_index(drop=True, inplace=True)
# What it does:
# - *reset_index()* resets the index to default (0, 1, 2...).*drop=True* means "don’t add the old index as a column".
# *inplace=True* updates the DataFrame directly.


df['customer_id'] = range(1, len(df) + 1)
# This will overwrite the existing Customer_ID column with new values starting from 1.
print(df)




"""CHALLANGES ENCOUNTERD
AFTER DROPPIN, THE INDEXES TENDS TO RESET
THE INDEX TENDS TO OVERRRIDE 
I ENCOUNTERD NEGATIVE VALUES IN QUANTITY and price"""



df.to_csv(r"C:\Users\LENOVO\Desktop\PYHON _ASSIGNMENTS\Assignment6\cleaned_sales_data3.csv", index=False)
print("\nFILE LOADED.....")



