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

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print("request body:", r.request.body)
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)