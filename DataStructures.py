# LISTS

# The `append()` method is used to add an element to the end of a list.
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)

# The `copy()` method is used to create a shallow copy of a list.
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list)

# The `count()` method is used to count the number of occurrences of a specific element in a list in Python.
count_list = [1, 2, 2, 3, 4, 2, 5, 2]
count = count_list.count(2)
print(count)

# The `del` statement is used to remove an element from list. `del` statement removes the element at the specified index.
del_list = [10, 20, 30, 40, 50]
del del_list[2]
print(del_list)

# The `extend()` method is used to add multiple elements to a list. It takes an iterable (such as another list, tuple, or string) and appends each element of the iterable to the original list.
fruits_list = ["apple", "banana", "orange"]
more_fruits = ["mango", "grape"]
fruits_list.extend(more_fruits)
print(fruits_list)

# The `insert()` method is used to insert an element.
insert_list = [1, 2, 3, 4, 5] 
insert_list.insert(2, 6) 
print(insert_list)

# You can use indexing to modify or assign new values to specific elements in the list.
mod_list = [10, 20, 30, 40, 50] 
mod_list[1] = 25
print(mod_list) 

# `pop()` method is another way to remove an element from a list in Python. It removes and returns the element at the specified index. If you don't provide an index to the `pop()` method, it will remove and return the last element of the list by default
pop_list = [10, 20, 30, 40, 50] 
removed_element = pop_list.pop(2)
print(removed_element) 
print(pop_list) 

# The `reverse()` method is used to reverse the order of elements in a list
rev_list = [1, 2, 3, 4, 5] 
rev_list.reverse() 
print(rev_list) 

# You can use slicing to access a range of elements from a list.
slice_list = [1, 2, 3, 4, 5] 
print(slice_list[1:4]) 
print(slice_list[:3]) 
print(slice_list[2:]) 
print(slice_list[::2]) 

# The `sort()` method is used to sort the elements of a list in ascending order. If you want to sort the list in descending order, you can pass the `reverse=True` argument to the `sort()` method.
sort_list = [5, 2, 8, 1, 9] 
sort_list.sort(reverse=True) 
print(sort_list) 

# TUPLES

# The sum() function in Python can be used to calculate the sum of all elements in a tuple, provided that the elements are numeric (integers or floats).
numbers = (10, 20, 5, 30)
print(sum(numbers))

# Find the smallest (min()) or largest (max()) element in a tuple.
num = (10, 20, 5, 30)
print(min(num))  
print(max(num))