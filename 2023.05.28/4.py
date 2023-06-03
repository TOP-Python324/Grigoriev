one = str(input())
tow = str(input())

figure_1 = one [1] 
figure_2 = tow [1]

if int(figure_1) % 2 == 0 and int(figure_2) % 2 != 0 or int(figure_1) % 2 != 0 and int(figure_2) % 2 == 0:
    print('Да')
else:
    print('Нет')

# Ввод:
# a1
# b2
# Вывод:
# Да

# Ввод:
# a1
# b1
# Вывод:
# Нет