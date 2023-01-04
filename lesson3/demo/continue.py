# Continue (or pass)
grains=['oat', 'rice', 'rye', 'wheat']
for item in grains:
  if item=='rice':
    continue
  else:
    print(item, end=' ')

# oat rye wheat