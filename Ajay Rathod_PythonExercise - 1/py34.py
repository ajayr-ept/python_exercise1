# Write a Python program to drop empty(None) Items from a given Dictionary.
# Original Dictionary - {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}

dic = {'c1':'Red','c2':'Green','c3':'None'}
print('original : ',dic)
dic.pop('c3')
print('new dictionary : ',dic)
