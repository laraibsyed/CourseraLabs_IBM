import pandas as pd
import requests

# URL of the Excel file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

# Download the Excel file
response = requests.get(url)
filename = "file_example_XLSX_10.xlsx"

# Write the content to a file
with open(filename, "wb") as f:
    f.write(response.content)

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(filename)

# Display the DataFrame
print(df)
