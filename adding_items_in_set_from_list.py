"""
Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
"""

set_var={"Python", "Django", "JavaScript"}
list=["Java", "C"]
print('elements in set before adding list elements :',set_var)

set_var.update(list)
print('elements in set after adding list elements :',set_var)