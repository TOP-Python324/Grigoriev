number = int(input())

# КОММЕНТАРИЙ: цифра — digit, число — number, num
first_digit = number // 100
second_digit = number % 10
third_digit = (number % 100) // 10

sum_numbers = first_digit + second_digit + third_digit
product_numbers = first_digit * second_digit * third_digit

print(f'Сумма цифр = {sum_numbers}\nПроизведение цифр = {product_numbers}')
# print(f'Произведение цифр = {product_numbers}')


# ДОБАВИТЬ: результат выполнения программы с собственными данными — в закомментированном виде
# 333
# Сумма цифр = 9
# Произведение цифр = 27

# ИТОГ: хорошо, но нужно лучше — 1/3
