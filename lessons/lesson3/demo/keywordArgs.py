def printID(name, **kwargs):
  print('Student Name: ', name, sep='')
  for key in kwargs:
    print(key, ': ', kwargs[key], sep='')

printID(name='Mary', id='8776', major='ECE')

'''
Student Name: Mary
id: 8776
major: ECE
'''