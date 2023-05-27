number = int(input())

# КОММЕНТАРИЙ: цифра — digit, число — number, num
first_number = number // 100
second_number = number % 10
third_number = (number % 100) // 10

sum_numbers = first_number + second_number + third_number
product_numbers = first_number * second_number * third_number

print(f'Сумма цифр = {sum_numbers}')
print(f'Произведение цифр = {product_numbers}')


# ДОБАВИТЬ: результат выполнения программы с собственными данными — в закомментированном виде


# ИТОГ: хорошо, но нужно лучше — 1/3
