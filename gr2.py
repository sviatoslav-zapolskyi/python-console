# Введення даних
# name = input("Введіть ім'я: ")
# surname = input("Введіть прізвище: ")

name = "Святослав"
surname = "Запольський"


# Кількість літер
A = len(name)
B = len(surname)

print("Кількість літер в імені:", A)
print("Кількість літер в прізвищі:", B)

# Лінійна частина
C = A + B
print("C = ", C)

D = A * B
print("D = ", D)

# Галуження
if C > 10:
    E = D + C
else:
    E = D - C

print("E = ", E)

# Цикл
F = 0

for i in range(0, A + 1):
    F = F + E
    print("F = ", F)

# Результат
R = F - B

print("Результат:", R)