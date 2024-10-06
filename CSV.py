import pandas as pd
import seaborn as sb
import numpy as np
import requests
import lxml
import openpyxl

# URL of the CSV file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

# Download the CSV file
response = requests.get(url)
filename = "addresses.csv"

# Write the content to a CSV file
with open(filename, "wb") as f:
    f.write(response.content)

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(filename, header=None)

# Display the DataFrame
print(df)

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

# To select the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name" ]

# To select the 0th,1st and 2nd row of "First Name" column only
df.iloc[[0,1,2], 0]

df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df = df.transform(func = lambda x : x + 10)
result = df.transform(func = ['sqrt'])
print(result)