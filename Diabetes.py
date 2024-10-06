import pandas as pd
import requests
import matplotlib.pyplot as plt

# URL of the dataset
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

# Download the CSV file
response = requests.get(url)
filename = "diabetes.csv"

# Save the content to a CSV file
with open(filename, "wb") as f:
    f.write(response.content)

# Load the data into a DataFrame
df = pd.read_csv(filename, header=None)

# Display the first 5 rows of the DataFrame
print("The first 5 rows of the dataframe: \n", df.head(5))

# Check for missing data
missing_data = df.isnull()
print("\nMissing data in the DataFrame:\n", missing_data.head(5))

# Count and display missing values for each column
for column in missing_data.columns:
    print(f"Missing values in column '{column}':")
    print(missing_data[column].value_counts())
    print("")    

# Verify the column indices and the Outcome column
print("\nColumn Indices and First Values:")
for i in range(df.shape[1]):
    print(f"Column {i}: {df[i].head(1)}")

# Set the index for the Outcome column
outcome_col_index = 8

# Check the value counts for the Outcome column
outcome_counts = df[outcome_col_index].value_counts()
print("\nOutcome Value Counts:")
print(outcome_counts)

# Define labels for the pie chart
labels = ['Not Diabetic', 'Diabetic']

# Ensure the number of labels matches the value counts
if len(outcome_counts) != len(labels):
    print("Mismatch in the number of labels and value counts.")
else:
    # Visualize the distribution of diabetes outcomes
    plt.figure(figsize=(8, 6))
    plt.pie(outcome_counts, labels=labels, autopct='%0.2f%%', startangle=90)
    plt.title('Distribution of Diabetes Outcomes')
    plt.legend()
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.show()
