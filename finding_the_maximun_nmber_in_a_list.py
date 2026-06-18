numberList= [10,12,5,7,9,18,22]
max= numberList[0]
for number in numberList:
  if max < number:
    max = number
print(max)