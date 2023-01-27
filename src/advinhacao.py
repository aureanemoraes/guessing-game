import random

print("********************")
print("Jogo de adivinhação")
print("********************\n")

# numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1,101)

# print("Número secreto: {}".format(numero_secreto))
print(f'Número secreto: {numero_secreto}')

total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("\nTentativa {} de {}".format(rodada, total_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")

    print("Você digitou", chute_str)

    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("\nVocê digitou um número inválido. Digite um número entre 1 e 100")
        continue

    acertou     = chute == numero_secreto
    maior       = chute > numero_secreto
    menor       = chute < numero_secreto 

    print("")

    if (chute == numero_secreto):
        print("Você acertou! :D")
        break
    else:
        if (maior):
            print("Você errou... :( \nO número é maior que o valor correto.")
        elif (menor):
            print("Você errou.. :( \nO número é menor que o valor correto.")
        else:
            print("Você errou... :(")
        
    rodada += 1

print("\n\n!!!Fim do jogo!!!")
