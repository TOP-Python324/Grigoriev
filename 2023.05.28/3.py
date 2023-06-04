year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Да')
else:
    print('Нет')


# 2020
# Да

# 2021
# Нет


# ИТОГ: отлично — 3/3
