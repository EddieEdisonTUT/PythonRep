numero = int(input('numero: ')) # Шестизначне число
a = numero % 10
numero //= 10
#print(numero)
b = numero % 10
numero //= 10
#print(numero)
c = numero % 10
numero //= 10
#print(numero)
d = numero % 10
numero //= 10
#print(numero)
e = numero % 10
numero //= 10
#print(numero)
f = numero % 10
numero //= 10
#print(numero)
if (f == 0 or numero):
    print('Помилка вводу')
else:
    f,a = a,f
    e,b = b,e
    res = (f*100000 + e*10000 + d*1000 + c*100 + b*10 + a)
    print(res) #f7 e2 d3 c8 b9 a5 треба f5 e9 d3 c8 b2 a7

