numberList=[12,34,6,4,87,54]
min=numberList[0]
for number in numberList:
  if min > number:
    min = number
print(min)