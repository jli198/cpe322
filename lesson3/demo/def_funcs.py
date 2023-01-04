def printList(list):
  print('{:d} items on the list:'.format(len(list)))
  for item in list:
    print(item, end=' ')

def averageGrade(dict):
  sum=0.0
  for key in dict:
    sum=sum+dict[key]['grade']
  average=sum/len(dict)
  return average

averageGrade(students)
exit()