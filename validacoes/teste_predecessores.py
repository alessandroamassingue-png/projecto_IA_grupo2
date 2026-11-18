
from dominio import ProblemaFerry


def testar_predecessores():

    problema = ProblemaFerry()

    # Estado inicial
    estado_inicial = problema.estado_inicial()

    # Obter uma acção possível
    accoes = problema.accoes(estado_inicial)

    accao = accoes[0]

    # Avançar para um novo estado
    estado_seguinte = problema.resultado(
        estado_inicial,
        accao
    )

    print("Estado inicial:", estado_inicial)
    print("Acção realizada:", accao)
    print("Estado seguinte:", estado_seguinte)

    # Obter os predecessores
    anteriores = problema.predecessores(
        estado_seguinte
    )

    print("\nPredecessores encontrados:")

    for estado, accao_reversa in anteriores:
        print("Estado:", estado)
        print("Acção:", accao_reversa)

    # Confirmar se o estado inicial está entre os predecessores
    estados_anteriores = {
        estado for estado, _ in anteriores
    }

    if estado_inicial in estados_anteriores:
        print("\nTESTE APROVADO!")
        print("A transição pode ser revertida.")
    else:
        print("\nTESTE FALHOU!")


if __name__ == "__main__":
    testar_predecessores()
