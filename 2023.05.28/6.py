# ИСПРАВИТЬ: преобразование в str избыточно
one = str(input())
tow = str(input())

# ИСПОЛЬЗОВАТЬ: метод index() работает и со строками
# letters = ['a','b','c','d','e','f','g','h']
letters = 'abcdefgh'

one_i = int(one[1])
one_p = one_i + 1
one_m = int(one[1]) - 1
tow_i = int(tow[1])

one_w_in = letters.index(str(one[0]))
one_w_p = one_w_in+1
one_w_m = one_w_in-1

tow_w_in = letters.index(str(tow[0]))

# ИСПРАВИТЬ: не всё проверили, опять с горизонталями проблема (см. пример ниже)
if one_w_in == tow_w_in and one_p == tow_i or one_m == tow_i or one_i == tow_i and one_w_p == tow_w_in or one_w_m == tow_w_in:
    print("Да")
else:
    print("Нет")

# СДЕЛАТЬ: модуль числа в Python реализован во встроенной функции abs(), а перейти от символа к числу можно с помощью встроенной же функции ord(), которая возвращает код любого символа из таблицы UTF-8


# b2
# a2
# Да

# b3
# с1
# Нет

# b3
# a1
# КОММЕНТАРИЙ: должно быть Нет
# Да


# ИТОГ: переделать — 2/5
