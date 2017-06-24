# -*- coding: utf-8 -*-
# random sales dictionary
sales = { 'grapes': 4, 'orange': 3, 'apple': 8 }

print(sales.items())

# random sales dictionary
print(sales.values())


items = sales.items()
print('Original items:', items)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)
print('Updated values:', sales.values())

person = {'name': 'Phill', 'age': 22, }

print('Before dictionary is updated')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)