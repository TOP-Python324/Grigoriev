integer = int(input())
fractional = int(input())

# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше двух (см. пример ниже) — придумайте более универсальное решение
magic = fractional / 10
summa = integer + magic

kmh = summa * 1.61

# КОММЕНТАРИЙ: если результат округления должен быть использован где-то ещё, тогда используете функцию round(); в данном случае выгоднее воспользоваться синтаксисом f-строк
r = round(kmh, ndigits=1)
print(f'{summa} миль = {r} км')


# 5
# 81
# КОММЕНТАРИЙ: а должно быть 5.81 миль
# 13.1 миль = 21.1 км


# ИТОГ: доработать — 2/5
