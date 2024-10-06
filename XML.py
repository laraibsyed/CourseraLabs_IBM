import pandas as pd
import requests
import xml.etree.ElementTree as ET

# Step 1: Download the XML file using requests
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"
response = requests.get(url)

# Save the file locally
with open("Sample-employee-XML-file.xml", "wb") as f:
    f.write(response.content)

# Step 2: Parse the XML file using ElementTree
tree = ET.parse("Sample-employee-XML-file.xml")
root = tree.getroot()

# Step 3: Define the columns for the DataFrame
columns = ["firstname", "lastname", "title", "division", "building", "room"]
datatframe = pd.DataFrame(columns=columns)

# Iterate through each node in the XML root
for node in root:
    firstname = node.find("firstname").text if node.find("firstname") is not None else None
    lastname = node.find("lastname").text if node.find("lastname") is not None else None
    title = node.find("title").text if node.find("title") is not None else None
    division = node.find("division").text if node.find("division") is not None else None
    building = node.find("building").text if node.find("building") is not None else None
    room = node.find("room").text if node.find("room") is not None else None
    
    # Create a DataFrame for the current row
    row_df = pd.DataFrame([[firstname, lastname, title, division, building, room]], columns=columns)
    
    # Concatenate with the existing DataFrame
    datatframe = pd.concat([datatframe, row_df], ignore_index=True)

# Display the final DataFrame
print(datatframe)

# Herein xpath we mention the set of xml nodes to be considered for migrating  to the dataframe which in this case is details node under employees.
df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 
datatframe.to_csv("employee.csv", index=False)