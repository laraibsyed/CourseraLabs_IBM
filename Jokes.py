import requests
import pandas as pd
import json

url = "https://official-joke-api.appspot.com/jokes/ten"

data = requests.get(url)

results = json.loads(data.text)

df = pd.DataFrame(results)

df.drop(columns=["type","id"],inplace=True)
print(df)