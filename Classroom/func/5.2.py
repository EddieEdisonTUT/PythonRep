def print_zirochky(n):
    if n == 0:
        return
    print('*', end='')
    print_zirochky(n - 1)

n = int(input('Введіть довжину лінії: '))

print_zirochky(n)