from bs4 import BeautifulSoup
import requests

url = "https://www.ibm.com"

data = requests.get(url).text

soup = BeautifulSoup(data, "html5lib")

for link in soup.find_all("a", href=True):
    print(link.get("href"))

for pic in soup.find_all("img"):
    print(pic)
    print(pic.get("src"))

url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data2 = requests.get(url2).text
soup2 = BeautifulSoup(data2, "html5lib")
table = soup2.find('table')
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))