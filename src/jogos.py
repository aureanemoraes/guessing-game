import forca
import advinhacao

print("********************")
print("Selecione um jogo")
print("********************\n")

while(True):
    print("(1) Jogo da forca")
    print("(2) Jogo da adivinhação")
    jogo_selecionado = int(input("Insira a opção desejada: "))
    if (jogo_selecionado == 1):
        forca.jogar()
        break
    elif (jogo_selecionado == 2):
        advinhacao.jogar()
        break
    else:
        print("Opção inválida! Por favor, tente novamente.")