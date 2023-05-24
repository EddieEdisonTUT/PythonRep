def draw_square(length, symbol, filled):
    if filled:
        for i in range(length):
            print(symbol * length)
    else:
        print(symbol * length)
        for i in range(length - 2):
            print(symbol + ' ' * (length - 2) + symbol)
        print(symbol * length)

# Виклик функції з різними параметрами
draw_square(5, '*', True)
print()
draw_square(5, '*', False)

