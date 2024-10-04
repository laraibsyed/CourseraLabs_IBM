import requests
import json
import pandas as pd


data = requests.get("https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)

pd.DataFrame(results)
df = pd.json_normalize(results)
print(df)

cherry = df.loc[df["name"] == 'Cherry']
print(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

cal_banana = df.loc[df["name"] == 'Banana']
print(cal_banana.iloc[0]['nutritions.calories'])