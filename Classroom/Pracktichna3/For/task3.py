a = int(input('Введіть першу границю: '))
b = int(input('Введіть другу границю: '))
c = int(input('Введіть обране число: '))


for i in range(a,b+1):
    if i == c:
        print('!',i,'!', end=' ')
    else:
        print(i, end=' ')
    
    
    