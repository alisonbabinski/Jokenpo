import resultados

def verificacaoPedra(adv, vit, emp, der, vencedor):
    if adv == 1:
        resultados.empatou()
        vencedor.append("Empate")
        emp += 1
    if adv == 2:
        resultados.perdeu()
        vencedor.append("Computador")
        der += 1
    if adv == 3:
        resultados.ganhou()
        vencedor.append("Usuário")
        vit += 1
    return adv, vit, emp, der, vencedor


def verificacaoPapel(adv, vit, emp, der, vencedor):
    if adv == 1:
        resultados.ganhou()
        vencedor.append("Usuário")
        vit += 1
    if adv == 2:
        resultados.empatou()
        vencedor.append("Empate")
        emp += 1
    if adv == 3:
        resultados.perdeu()
        vencedor.append("Computador")
        der += 1
    return adv, vit, emp, der, vencedor

def verificacaoTesoura(adv, vit, emp, der, vencedor):
    if adv == 1:
        resultados.perdeu()
        vencedor.append("Computador")
        der += 1
    if adv == 2:
        resultados.ganhou()
        vencedor.append("Usuário")
        vit += 1
    if adv == 3:
        resultados.empatou()
        vencedor.append("Empate")
        emp += 1
    return adv, vit, emp, der, vencedor