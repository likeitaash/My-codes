# Question:
"""
By using list comprehension, please write a program to print the list after removing the value 24 in 
[12,24,35,24,88,120,155].
"""
# Hints:
"""
Use list's remove method to delete a value.
"""
aa = [12, 24, 35, 24, 88, 120, 155]
aa = [x for x in aa if x != 24]
print(aa)
