manager1 = int(input('Менеджер 1: '))
manager2 = int(input('Менеджер 2: '))
manager3 = int(input('Менеджер 3: '))
stavka = 200
if manager1 < 500:
    print('Зарплатня М1:',(manager1 * 0.02) + stavka)
elif manager1 >= 500 and manager1 < 1000:
    print('Зарплатня М1:',(manager1 * 0.05) + stavka)
elif manager1 > 1000:
    print('Зарплатня М1:',(manager1 * 0.08) + stavka)
if manager2 < 500:
    print('Зарплатня М2:',(manager2 * 0.02) + stavka)
elif manager2 >= 500 and manager2 < 1000:
    print('Зарплатня М2:',(manager2 * 0.05) + stavka)
elif manager2 > 1000:
    print('Зарплатня М2:',(manager2 * 0.08) + stavka)
if manager3 < 500:
    print('Зарплатня М3:',(manager3 * 0.02) + stavka)
elif manager3 >= 500 and manager3 < 1000:
    print('Зарплатня М3:',(manager3 * 0.05) + stavka)
elif manager3 > 1000:
    print('Зарплатня М3:',(manager3 * 0.08) + stavka)