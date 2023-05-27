integer = int(input())
fractional = int(input())

# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше двух (см. пример ниже) — придумайте более универсальное решение
if fractional <= 9 and 1 <= fractional:
    magic = fractional / 10
    summa = integer + magic
    control = round(summa, ndigits=2)
    kmh = control * 1.61
    r = round(kmh, ndigits=2)
    print(f'{control} миль = {r} км')
if fractional <= 99 and 10 <= fractional:
    magic = fractional / 100
    summa = integer + magic
    control = round(summa, ndigits=2)
    kmh = control * 1.61
    r = round(kmh, ndigits=2)
    print(f'{control} миль = {r} км')
if fractional <= 999 and 100 <= fractional:
    magic = fractional / 1000
    summa = integer + magic
    control = round(summa, ndigits=2)
    kmh = control * 1.61
    r = round(kmh, ndigits=1)
    print(f'{control} миль = {r} км')

# КОММЕНТАРИЙ: если результат округления должен быть использован где-то ещё, тогда используете функцию round(); в данном случае выгоднее воспользоваться синтаксисом f-строк

# Пример ввода:
# 15
# 7
# Пример вывода:
# 15.7 миль = 25.3 км

# 5
# 81
# КОММЕНТАРИЙ: а должно быть 5.81 миль
# 13.1 миль = 21.1 км
# Исправлено
# 5
# 81
# 5.81 миль = 9.35 км


# ИТОГ: доработать — 2/5

