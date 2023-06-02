one = int(input())
tow = int(input())

delen = one % tow

if delen == 0:
    print(f'{one} делиться на {tow} нацело'
    f'\n частное: {one // tow}')
else:
    print(f'{one} не делиться на {tow} нацело'
    f'\n не полное частное: {one // tow}'
    f'\n остаток: {one % tow}')