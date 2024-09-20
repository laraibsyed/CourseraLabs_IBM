inventory = {}

ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020

inventory["ProductNo1"] = ProductNo1
inventory["ProductNo1_quantity"] = ProductNo1_quantity
inventory["ProductNo1_price"] = ProductNo1_price
inventory["ProductNo1_releaseYear"] = ProductNo1_releaseYear

ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear= 2023

inventory["ProductNo2"] = ProductNo2
inventory["ProductNo2_quantity"] = ProductNo2_quantity
inventory["ProductNo2_price"] = ProductNo2_price
inventory["ProductNo2_releaseYear"] = ProductNo2_releaseYear

print(inventory)

"ProductNo1_releaseYear" in inventory
"ProductNo2_releaseYear" in inventory

del(inventory["ProductNo1_releaseYear"])
del(inventory["ProductNo2_releaseYear"])