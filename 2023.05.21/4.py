number = int(input())

first_number = number // 100
second_number = number % 10
third_number = (number % 100) // 10

sum_numbers = first_number + second_number + third_number

product_numbers = number // sum_numbers

print(f'Сумма цифр = {sum_numbers}')

print(f'Произведение цифр = {product_numbers}')
