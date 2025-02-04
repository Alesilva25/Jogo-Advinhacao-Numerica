from colorama import init, Fore as fr
import random

init()
yellow = fr.YELLOW
green = fr.GREEN
default = fr.WHITE
red = fr.RED

print(f"{yellow}Seja muito bem vindo ao Guess Number do Ale!")
choice_number = int(input("Digite o número teto do desafio: "))

random_number = random.randint(0, choice_number)

while True:
    answer_user = int(input("\nAdvinhe o número: "))
    if answer_user == random_number:
        print(f"{green}Acertou!")
        break
    elif answer_user > random_number:
        print(f"{red}Chutou alto, o número aleatório é menor que isso...")
    elif answer_user < random_number:
        print(f"{red}Chutou baixo, o número aleatório é maior que isso...")