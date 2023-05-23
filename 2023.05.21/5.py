integer = int(input())
fractional = int(input())

magic = fractional / 10

summa = integer + magic

kmh = summa * 1.61

r = round(kmh, ndigits= 1)

print(f'{summa} миль = {r} км')