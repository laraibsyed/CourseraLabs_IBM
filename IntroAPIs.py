import requests
import os
from PIL import Image
from IPython.display import IFrame


URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(), "example19.txt")

r = requests.get(URL)
with open(path, "wb") as f:
    f.write(r.content)

print(f"File downloaded successfully to: {path}")
