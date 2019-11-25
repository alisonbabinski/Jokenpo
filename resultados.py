def ganhou():
    print("\033[32m"+"VOCE GANHOU! :D"+"\033[0;0m")

def perdeu():
    print("\033[31m"+"VOCE PERDEU :("+"\033[0;0m")

def empatou():
    print("\033[34m"+"EMPATE! Tente novamente"+"\033[0;0m")

def placar(vit, der):
    print("Placar - Você {} x {} Computador ".format(vit, der))