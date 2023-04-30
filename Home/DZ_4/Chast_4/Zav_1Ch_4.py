import time
import math
a = int(input('number1: '))
b = int(input('number2: '))

if a < 2:
    a = 2
start_time = time.time()
for i in range(a,b+1):
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            # print('Прості',j)
            break
    else:
        print(i, end=' ')
end_time = time.time()
print('\ntime = ',end_time - start_time)