# Remove duplicates namess

names = ["Abisheek", "Abisheek", "John", "Alice", "John", "Bob"]
unique_names = list(set(names))
print(unique_names)


#Student mark using set

marks = {85, 90, 78, 92, 88, 90, 85}
print("Unique marks:", marks)
print("Number of unique marks:", len(marks))
print("highest mark:", max(marks))
print("lowest mark:", min(marks))

'''
['Alice', 'John', 'Abisheek', 'Bob']
Unique marks: {85, 88, 90, 92, 78}
Number of unique marks: 5
highest mark: 92
lowest mark: 78
'''