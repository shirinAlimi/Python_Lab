fruits = ["Apple", "Banana", "Mango"]
print("Original list: ", fruits)

# append() - adds an element at the end
fruits.append("Orange")
print("append:", fruits)

# insert() - inserts an element at a specific position
fruits.insert(1, "Grapes")
print("insert:", fruits)

# remove() - removes a specific element
fruits.remove("Banana")
print("remove:", fruits)

# pop() - removes and returns an element by index
removed_item = fruits.pop(2)
print("pop:", fruits)
print("Removed item:", removed_item)

# copy() - creates a copy of the list
new_fruits = fruits.copy()
print("copy:", new_fruits)

# clear() - removes all elements from the list
fruits.clear()
print("clear:", fruits)