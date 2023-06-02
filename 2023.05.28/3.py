year = int(input())

if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Да')
else:
    print('Нет')

# Ввод:

# 2020

# Вывод:
# Да


# Ввод:
# 2021

# Вывод:
# Нет