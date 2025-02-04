import random

def real_number(number):
    for i in range(1, 10, 1):
        number = random.randint(i)
        return number

your_number = int(input("Digite seu número: "))

if your_number == real_number:
    print("certo")
else:
    print("errado")