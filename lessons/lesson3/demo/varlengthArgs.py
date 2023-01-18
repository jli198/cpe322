def printID(name, *varargs):
  print('Student Name:', name)
  for item in varargs:
    print(item)

printID('Barb')
printID('Mary', 'id: 8776', 'major: ECE')
exit()

'''
Student Name: Barb
Student Name: Mary
id: 8776
major: ECE
'''