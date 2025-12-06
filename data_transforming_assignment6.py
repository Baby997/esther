'''assignment on cleaned_sales_data

================================COMPLETE TRANSFORMATION PIPELINE=============================

=============================TRANSFORM CLEANED DATASET TO ANALYSIS-READY FORMAT========================

from cleaned csv file (sales_data.csv)

'''


'''PART 1: COLUMN MANAGEMENT
Rename columns to snake_case
ie. making the column in a consisent format like conv to lowercase, remove whitespace
empty str, etc
'''
import pandas as pd
cleaned_sales_data = pd.read_csv(r"C:\Users\LENOVO\Desktop\PYHON _ASSIGNMENTS\Assignment6\cleaned_sales_data3.csv")
df = pd.DataFrame(cleaned_sales_data)
#print(df)


(
    df.columns
    .str.strip()                     # remove leading/trailing spaces
    .str.lower()                    # lowercase
    .str.replace(' ', '_')          # replace spaces with underscore
    .str.replace('[^0-9a-zA-Z_]', '', regex=True)  # remove special characters

)


print(df[['price', 'quantity']].head())        # View sample data
print(df.columns)                              # Check if column names are duplicated/misaligned
df.info()                                      # See if the dtypes match expectations






'''=====================================PART 2=========================================


Standardization
standardize category: Lowercase, no spaces, fix misspelling'''
#Convert to lowercase and remove spaces
df['category'] = df['category'].str.lower().str.replace(' ', '_')

#fix  misspellings 
df['category'] = df['category'].replace({
    'Atr': 'Art',
    #misspelled : correctspelling
    'Stationary': 'Stationery',
})






'''======================================PART 3=====================================
Type conversion
Convert purchase_date to datetime
purchase_date[ns]'''


df['purchase_date'] = pd.to_datetime(df['purchase_date'])



'''format serves several key purposes:
1. Accurate Time-Based Analysis=================  
   Enables filtering, grouping, and sorting by year, month, day, etc.
2. Date Operations============ 
   Lets you perform operations like calculating time differences (e.g., days since purchase).
3. Plotting Time Series================  
   Libraries like Matplotlib or Seaborn require datetime format for time-based visualizations.
4. Avoiding Errors==================  
   Prevents issues caused by treating dates as plain strings (e.g., wrong sort order).
5. Consistency=================  
   Standardizes format across datasets, useful when merging or joining data.
'''


'''=======Ensure "price" and "quantity" are numeric'''
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')


'''pd.to_numeric() converts values to numeric types (like int or float).
- errors='coerce' turns any non-numeric or invalid values into NaN, which you can later handle (e.g., drop or fill).
this is dpne so that numeric/mathematical operations can be done accuratley'''



'''======Convert category and gender to category dtype (they both have diff categories of data in their cels)'''
df['category'] = df['category'].astype('category')
df['gender'] = df['gender'].astype('category')

'''==============convert age in float to int dtype '''
df['age'] = df['age'].astype(int)

'''
The .astype() method in pandas is used to change the data type of a column in a DataFrame.

Example usage:
df['Age'] = df['Age'].astype(int)
What it does:
- Converts the values in the 'Age' column to integers.

Why it's useful:
- Ensures data is in the correct format for analysis.
- Reduces memory usage (e.g., converting to category).
- Prevents errors during calculations or visualizatio'''






'''========================================PART 4===================================='''


'''========get a column "subtotal" by price x quantity'''
df['subtotal'] = df['price'].round(2) * df['quantity']


'''===========column "vat by subtotal x 0.075'''
df['vat'] = (df['subtotal'] * 0.075).round(2)


'''============column "total amount" by subtotal + vat'''
df['total_amount'] = df['subtotal'] + df['vat'].round(2)
# print(df)
# print(df.dtypes)

''''price_tier'''
#Define price bins and tier labels
bins = [0, 1000, 3000, float('inf')]
labels = ['budget', 'standard', 'premium']

#Create the price_tier column
df['price_tier'] = pd.cut(df['price'], bins=bins, labels=labels)

'''bins = [0, 1000, 3000, float('inf')]
#This creates ranges for grouping price values:
#- 01000 → budget  
#- 1000-3000 → standard  
#- 3000+ → premium  
#- float('inf') means "infinity" (no upper limit).

# 2. labels = ['budget', 'standard', 'premium']
# - These are the category names assigned to each range.

# 3. pd.cut(...)
# - pd.cut() is used to categorize continuous numeric data into bins.
# - It matches each df['price'] value to the appropriate bin, and returns the label.
'''



'''========================================PART 5====================================
==========Extract year, month, month_name'''
df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors='coerce')

#Extract year
df['year'] = df['purchase_date'].dt.year

#Extract month number
df['month'] = df['purchase_date'].dt.month

# Extract month_name
df['month_name'] = df['purchase_date'].dt.month_name()

'''Absolutely! Here's a breakdown of each method used in the code and what it does:

---

*1. pd.to_datetime()*

python
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')


- *pd.to_datetime()*: A pandas function that converts a column or list of strings (like '2025-11-24') into datetime objects.
- *errors='coerce'*: If a value can't be converted to a date (e.g., wrong format), it will turn into NaT (Not a Time), avoiding a crash.

*2. .dt accessor*
Used to access datetime properties from a column that has datetime values.

*3. .dt.month_name()*
df['month_name'] = df['Purchase_Date'].dt.month_name()
- *.dt.month_name()*: Extracts the full month name (e.g., "January", "August") from each datetime in the column.

*4. .dt.year*
df['year'] = df['Purchase_Date'].dt.year
- *.dt.year*: Extracts just the year (e.g., 2024, 2025) from each datetime object.

*5. .dt.month*
df['month'] = df['Purchase_Date'].dt.month
- *.dt.month*: Returns the numeric month (1 to 12) for each datetime value.
These methods help break down a date into parts (year, month, name of the month) for easier analysis and visualization.'''

# Extract day of the week
df['day_of_week'] = df['purchase_date'].dt.day_name()

# Extract Quaters
df['quarter'] = df['purchase_date'].dt.quarter

'''- .dt.day_name(): returns the full name of the day (e.g., "Monday", "Friday")
.dt.quater returns the quaters of the year(q1, q2, etc)
Note = to conduct all these using the
'''
# '''rename the col (pascal case)
# df.rename(columns={'column named to be replaced : column to replace with})'''
# df.rename(columns={ 
# 'customer_id': 'CustomerID', 
# 'product': 'ProductName', 
# 'price': 'Price', 
# 'quantity': 'Quantity' 
# }, inplace=True) 
# # After 
# print("Renamed:", df.columns.tolist())
# #tolist saves the col to list

'''Create sales season'''
# Extract month number
df['month'] = df['purchase_date'].dt.month

# Define sales season based on month
def get_season(month):
    if month in [12, 1, 2]:
        return 'Dry Season'
    elif month in [3, 4, 5]:
        return 'Planting Season'
    elif month in [6, 7, 8]:
        return 'Rainy Season'
    elif month in [9, 10, 11]:
        return 'Harvest Season'
    else:
        return 'Unknown'

df['sales_season'] = df['month'].apply(get_season)


'''Categorize age_group'''
bins = [0, 18, 30, 50, 100]
labels = ['Teen', 'Young Adult', 'Adult', 'Senior']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

'''Categorize quantity_level'''
def quantity_level(qty):
    if qty < 50:
        return 'Low'
    elif 50 <= qty < 100:
        return 'Medium'
    elif qty >= 100:
        return 'High'
    else:
        return 'Unknown'

df['quantity_level'] = df['quantity'].apply(quantity_level)

'''Create customer_segment'''
df['customer_segment'] = df['age_group'].astype(str) + '_' + df['gender'].str.capitalize()




'''===============================PART 7==========================='''
'''Verify no missing in critical columns'''
critical_columns = ['customer_id', 'customer_name', 'gender', 'age', 'price', 'quantity', 'purchase_date']
missing_check = df[critical_columns].isnull().sum()
print("Missing values in critical columns:\n", missing_check)

'''Display summary statistics'''
print("\nSummary statistics:")
print(df.describe(include='all'))

'''Show value counts for key categorical columns'''
print("\nGender distribution:")
print(df['gender'].value_counts())

print("\nAge group distribution:")
print(df['age_group'].value_counts())

print("\nQuantity level distribution:")
print(df['quantity_level'].value_counts())


print("\n==================CLEANED AMD TRANSFORMED DATA===========================")
print(df)

df.to_csv(r"C:\Users\LENOVO\Desktop\PYHON _ASSIGNMENTS\Assignment6\Transformed_sales_data_3.csv", index=False)