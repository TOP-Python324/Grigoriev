number = int(input())

first_digit = number // 100
second_digit = number % 10
third_digit = (number % 100) // 10

# УДАЛИТЬ: данные переменные используются каждая только единожды — оптимизируйте
sum_numbers = first_digit + second_digit + third_digit
product_numbers = first_digit * second_digit * third_digit

print(f'Сумма цифр = {sum_numbers}\n'
      f'Произведение цифр = {product_numbers}')


# 333
# Сумма цифр = 9
# Произведение цифр = 27


# ИТОГ: хорошо, ещё немного доработать — 2/3
