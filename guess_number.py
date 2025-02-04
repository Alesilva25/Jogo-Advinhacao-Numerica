from colorama import init, Fore as fr
import random

init()
yellow = fr.YELLOW
green = fr.GREEN
white = fr.WHITE
red = fr.RED

print(f"{yellow}Seja muito bem vindo ao Guess Number do Ale!\n")

random_number = random.randint(1, 10)
n_choices = 0

while True:
    answer_user = int(input(f"{white}\nAdvinhe um número de 1 a 10\nVocê tem 3 tentativas: "))
    n_choices = n_choices + 1
    if n_choices > 2:
        print(f"{red}Você perdeu!")
        break
    else:
        if answer_user == random_number:
            print(f"{green}Acertou!")
            break
        elif answer_user > random_number:
            print(f"{red}Chutou alto, o número aleatório é menor que isso...")
        elif answer_user < random_number:
            print(f"{red}Chutou baixo, o número aleatório é maior que isso...")

print(f"{yellow}Número de tentativas: {n_choices}")