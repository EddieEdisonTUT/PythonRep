i = 0
sum = 0 
for i in range(100,10000):
    i += 1
    
    if i % 11 == 0:
        sum += i
else:
    print(sum)