# ПЕРЕИМЕНОВАТЬ: клетка поля — square, field
# ИСПРАВИТЬ: функция input() всегда возвращает объект str, преобразование избыточно
one = str(input())
tow = str(input())

# ПЕРЕИМЕНОВАТЬ: горизонталь — horizontal
figure_1 = one[1]
figure_2 = tow[1]

# ИСПРАВИТЬ: очень много повторов — преобразования в int, взятие остатков от деления — всё это необходимо вычислить заранее
# ИСПРАВИТЬ: почему только горизонтали проверяете? (см. примеры ниже)
if int(figure_1) % 2 == 0 and int(figure_2) % 2 != 0 or int(figure_1) % 2 != 0 and int(figure_2) % 2 == 0:
    print('Да')
else:
    print('Нет')

# СДЕЛАТЬ: совсем немного очень простой математики — о свойствах чётных и нечётных чисел — помогут вам заметно сократить количество логических выражений


# a1
# b2
# Да

# a1
# b1
# Нет

# a1
# c1
# КОММЕНТАРИЙ: должно быть Да
# Нет

# a1
# c2
# КОММЕНТАРИЙ: должно быть Нет
# Да


# ИТОГ: доработать — 2/6
