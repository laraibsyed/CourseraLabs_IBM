Shopping_List = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]
Shopping_List.append("Football")

print(Shopping_List) # Entire List

print(Shopping_List[0]) # First Index
print(Shopping_List[-1]) # Last Index

print(Shopping_List[1:3]) # Splicing

Shopping_List[3] = "Notebook"
print(Shopping_List) # Changing an index

del(Shopping_List[4])
print(Shopping_List) # Delete an index