"""
Write a python program to add items from another set to the current set. 
thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
"""

set_current={"Java", "Python", "SQL"}
set_another={"C", "Cpp", "NoSQL"}
print('current set before adding another set :',set_current)

set_current=set_current.union(set_another)
print('current set after adding another set :',set_current)
