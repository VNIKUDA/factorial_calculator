def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
    
print(" --- Факторіал числа --- ")

number = int(input("Введіть число: "))
result = factorial(number)

print(f"Факторіал числа {number} є {result}")