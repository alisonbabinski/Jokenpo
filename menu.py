from random import randint
import opcoes
import linhas
import verificacoes
import resultados
import relatorios

vencedor = []
ppt = 1
jog = 0 #total de jogos
adv = 0 #palpite do adversario
vit = 0 #total de vitórias
emp = 0 #total de empates
der = 0 #total de derrotas
opcoes.opcoes()
while ppt != 0:
    linhas.linhas()
    adv = (randint(1, 3))
    ppt = int(input("Digite o número conforme lista:"))
    if ppt > 0 and ppt < 4:
        jog += 1

        if adv == 1:
                print("O adversário mostrou"+"\033[36m"+" Pedra"+"\033[0;0m")
        elif adv == 2:
                print("O adversário mostrou"+"\033[35m"+" Papel"+"\033[0;0m")
        elif adv == 3:
                print("O adversário mostrou"+"\033[33m"+" Tesoura"+"\033[0;0m")


        if ppt == 1:
                print("Voce mostrou"+"\033[36m"+" Pedra"+"\033[0;0m")
                adv, vit, emp, der, vencedor = verificacoes.verificacaoPedra(adv, vit, emp, der, vencedor)
        elif ppt == 2:
                print("Voce mostrou"+"\033[35m"+" Papel"+"\033[0;0m")
                adv, vit, emp, der, vencedor = verificacoes.verificacaoPapel(adv, vit, emp, der, vencedor)
        elif ppt == 3:
                print("Voce mostrou"+"\033[33m"+" Tesoura"+"\033[0;0m")
                adv, vit, emp, der, vencedor = verificacoes.verificacaoTesoura(adv, vit, emp, der, vencedor)

        resultados.placar(vit, der)
    else:
        linhas.linhas()
        print("JOGO ENCERRADO!")
        print("Placar final")
        resultados.placar(vit, der)
        ppt = 0
linhas.linhas3()
relatorios.geral(jog,vit,emp,der)
relatorios.listagem_de_resultados(vencedor)