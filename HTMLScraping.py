from bs4 import BeautifulSoup
import requests

# html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# soup = BeautifulSoup(html, 'html5lib')
# print(soup.prettify())

# tag_object = soup.body
# print("Tag object: ", tag_object)

# tag_child = tag_object.h3
# print("Child: ", tag_child)

# parent_tag = tag_child.parent
# print("Parent: ", parent_tag)

# sibling_1=tag_object.next_sibling
# print("Sibling: ", sibling_1)

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, "html5lib")
rows = table_bs.find_all("tr")
print(rows)
first_row = rows[0]
print("First row: ", first_row)
tr_child = first_row.td
print("Child: ", tr_child)

for i,row in enumerate(rows):
    print("row",i,"is",row)

print("--------------------------")

for i,row in enumerate(rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

table_bs.find_all(id="flight")

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

table_bs.find_all(href=True)

table_bs.find_all(string="Florida")

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')
two_tables_bs.find("table")
two_tables_bs.find("table",class_='pizza')