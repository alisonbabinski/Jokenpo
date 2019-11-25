import linhas

def geral(jog, vit, emp, der):
    linhas.linhas3()
    print("RELATÓRIO GERAL")
    linhas.linhas()
    print("Partidas disputadas:", jog)
    print("\033[32m"+"Quantidade de Vitórias:", vit)
    pcvit = vit * 100 / jog
    float(str(pcvit))
    print(round(pcvit, 2), "% de vitórias")
    print("\033[34m"+"Quantidade de Empates", emp)
    pcemp = emp * 100 / jog
    float(str(pcemp))
    print(round(pcemp, 2), "% de empates")
    print("\033[31m"+"Quantidade de Derrotas", der)
    pcder = der * 100 / jog
    float(str(pcder))
    print(round(pcder, 2), "% de derrotas"+"\033[0;0m")


def listagem_de_resultados(vencedor):
    linhas.linhas3()
    print("RELATÓRIO DE RESULTADOS")
    print(vencedor)
    linhas.linhas()
