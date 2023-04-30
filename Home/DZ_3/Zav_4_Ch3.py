manager1 = int(input('Менеджер 1: '))
manager2 = int(input('Менеджер 2: '))
manager3 = int(input('Менеджер 3: '))
stavka = 200
if manager1 > manager2 and manager1 > manager3 and manager1 < 500:
    print('Кращій М1:',(manager1 * 0.03) + stavka + 200)
    if manager2 < 500 and manager3 < 500:
        print('M2:',(manager2 * 0.03) + stavka)
        print('M3:',(manager3 * 0.03) + stavka)
elif manager2 > manager1 and manager2 > manager3 and manager2 < 500:
    print('Кращій М2:',(manager2 * 0.03) + stavka + 200)
    if manager1 < 500 and manager3 < 500:
        print('M1:',(manager1 * 0.03) + stavka)
        print('M3:',(manager3 * 0.03) + stavka)
elif manager3 > manager1 and manager3 > manager2 and manager3 < 500:
    print('Кращій М3:',(manager3 * 0.03) + stavka + 200)
    if manager1 < 500 and manager2 < 500:
        print('M1:',(manager1 * 0.03) + stavka)
        print('M2:',(manager2 * 0.03) + stavka)
if manager1 > manager2 and manager1 > manager3 and manager1 >= 500 and manager1 < 1000:
    print('Кращій М1:',(manager1 * 0.05) + stavka + 200)
    if manager2 >= 500 and manager2 < 1000 and manager3 >= 500 and manager3 < 1000:
        print('M2:',(manager2 * 0.05) + stavka)
        print('M3:',(manager3 * 0.05) + stavka)
elif manager2 > manager1 and manager2 > manager3 and manager2 >= 500 and manager2 < 1000:
    print('Кращій М2:',(manager2 * 0.02) + stavka + 200)
    if manager1 >= 500 and manager1 < 1000 and manager3 >= 500 and manager3 < 1000:
        print('M1:',(manager1 * 0.05) + stavka)
        print('M3:',(manager3 * 0.05) + stavka)
elif manager3 > manager1 and manager3 > manager2 and manager3 >= 500 and manager3 < 1000:
    print('Кращій М3:',(manager3 * 0.02) + stavka + 200)
    if manager1 >= 500 and manager1 < 1000 and manager2 >= 500 and manager2 < 1000:
        print('M1:',(manager1 * 0.05) + stavka)
        print('M2:',(manager2 * 0.05) + stavka)
if manager1 > manager2 and manager1 > manager3 and manager1 > 1000:
    print('Кращій М1:',(manager1 * 0.08) + stavka + 200)
    if manager2 > 1000 and manager3 > 1000:
        print('M2:',(manager2 * 0.08) + stavka)
        print('M3:',(manager3 * 0.08) + stavka)
elif manager2 > manager1 and manager2 > manager3 and manager2 > 1000:
    print('Кращій М2:',(manager2 * 0.08) + stavka + 200)
    if manager1 > 1000 and manager3 > 1000:
        print('M1:',(manager1 * 0.08) + stavka)
        print('M3:',(manager3 * 0.08) + stavka)
elif manager3 > manager1 and manager3 > manager2 and manager3 > 1000:
    print('Кращій М3:',(manager3 * 0.08) + stavka + 200)
    if manager1 > 1000 and manager2 > 1000:
        print('M1:',(manager1 * 0.08) + stavka)
        print('M2:',(manager2 * 0.08) + stavka)