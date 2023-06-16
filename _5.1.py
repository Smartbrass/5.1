number = int(input("Введите целое число:"))
if (number > 0) and (number % 2) == 0:
    print("Положительное Четное")
elif (number < 0) and (number % 2) == 0:
    print("Отрицательное Четное")
elif (number < 0) and (number % 2) != 0:
    print("Отрицательное Нечетное")
elif (number > 0) and (number % 2) != 0:
    print("Положительное Нечетное")
else:
    print("Это Нуль")