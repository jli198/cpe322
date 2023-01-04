m=1
for n in range(4, 256, 4):
  m=m*n
  if m>512:
    break
  print(m)

'''
4
32
384
'''