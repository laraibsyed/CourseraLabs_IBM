import xlrd
import openpyxl
import pandas as pd

# Define the CSV file path (direct URL)
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'

# Read CSV file directly from the URL
df = pd.read_csv(csv_path)

# Check the first few rows of the DataFrame
print(df.head())

q = df[["Released", "Artist"]]
print(q)

print(df.iloc[1, 2])

new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index= new_index
df_new.loc['a', 'Artist']
print(df_new.loc['a':'d', 'Artist'])