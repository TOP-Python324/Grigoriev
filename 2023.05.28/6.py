one = str(input())
tow = str(input())
letters = ['a','b','c','d','e','f','g','h']

one_i = int(one[1])
one_p = one_i + 1
one_m = int(one[1]) - 1
tow_i = int(tow[1])

one_w_in = letters.index(str(one[0]))
one_w_p = one_w_in+1
one_w_m = one_w_in-1

tow_w_in = letters.index(str(tow[0]))

if one_w_in == tow_w_in and one_p == tow_i or one_m == tow_i or one_i == tow_i and one_w_p == tow_w_in or one_w_m == tow_w_in:
    print("Да")
else:
    print("Нет")
  
# Ввод:  
# b2
# a2
# Вывод:
# Да

# Ввод:  
# b3
# с1
# Вывод:
# Нет