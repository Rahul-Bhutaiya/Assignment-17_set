"""
Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}
"""

set_var={"Python", "Django", "JavaScript", 'SQL'}
print('values in set before removing last item("SQL") :',set_var)

set_var.discard('SQL')
print('values in set after removing last item("SQL") :',set_var)