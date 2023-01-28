import random

print("********************")
print("Jogo de adivinhação")
print("********************\n")

# numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1,101)
total_tentativas = 0
opcao_invalida = True

while (opcao_invalida == True):
    print('\n')
    print(f'Selecione o nível de dificuldade')
    print(f'(1) Fácil')
    print(f'(2) Intermediário')
    print(f'(3) Hardcore')
    nivel = int(input("Opção desejada: "))

    if (nivel == 1):
        total_tentativas = 20
        opcao_invalida = False
    elif (nivel == 2):
        total_tentativas = 10
        opcao_invalida = False
    elif (nivel == 3):
        total_tentativas = 5
        opcao_invalida = False
    else:
        print('\n')
        print('Opção inválida! Por favor, insira uma opção válida.')

# print("Número secreto: {}".format(numero_secreto))
print(f'Número secreto: {numero_secreto}')

pontuacao_atual = 200

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

        pontuacao_perdida = abs(numero_secreto - chute)
        pontuacao_atual = pontuacao_atual - pontuacao_perdida

        if (pontuacao_atual < 0):
            print('Você zerou os pontos. Game Over!')
            pontuacao_atual = 0
            break
        
    rodada += 1

print("\n\n!!!Fim do jogo!!!")
