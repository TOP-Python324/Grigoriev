number = int(input())

# УДАЛИТЬ: данные переменные используются каждая только единожды — неоптимально
hours = number // 60
minutes = number % 60

# ИСПРАВИТЬ: не хватает пробела: в случае если вы будете генерировать строку не для человека, а для другой функции/класса/программы — это может стоить вам неработающего приложения
print(f'{number}мин - это {hours} час {minutes} минут')


# ДОБАВИТЬ: результат выполнения программы с собственными данными — в закомментированном виде


# ИТОГ: хорошо, но нужно лучше — 1/3
