first_num = float(input())
second_num = float(input())
third_num = float(input())

# ДОБАВИТЬ: здесь нужна переменная, в которой вы будете накапливать необходимые значения

if first_num > 0:
    # ИСПРАВИТЬ здесь и далее: теряюсь в догадках о смысле прибавления ноля — совершенно лишнее действие
    one = first_num + 0
# УДАЛИТЬ: лишний блок, лишние действия
# КОММЕНТАРИЙ: если действовать в вашей логике создания дополнительных объектов, то их нужно было создать заранее сразу присвоив ноль, и менять значение только если выполнено условие, а если не выполнено то ноль и останется
else:
    one = first_num * 0

if second_num > 0:
    tow = second_num + 0
else:
    tow = second_num * 0

if third_num > 0:
    three = third_num + 0
else:
    three = third_num * 0

print(one + tow + three)


# КОММЕНТАРИЙ: примеры ввода/вывода в тексте задания нужны для самопроверки, а сюда нужно добавлять пример выполнения с собственными данными
# 4
# -22
# 1.5
# 5.5


# ИТОГ: нужно лучше, доработать — 1/3
