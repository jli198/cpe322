from lists import fruits
from dictionaries import student

#for v in s:
#   print(v, end= '')

i=0
for item in fruits:
  print('Fruit {:d}: {:s}'.format(i, item))
  i = i+1

for key in student:
  print('{:s}: {:s}'.format(key, student[key]))

'''
dict_keys(['1', '2', '3', '4', '5'])
Fruit 0: apple
Fruit 1: mango
Fruit 2: banana
Fruit 3: orange
name: Mary
id: 8776
'''