number1 = int (input('number: ')) #1297
a = number1 // 1000
h = number1 // 100 % 10
j = number1 // 10 % 10
g = number1 % 10
res = (g*1000+j*100+h*10+a)
print(res)