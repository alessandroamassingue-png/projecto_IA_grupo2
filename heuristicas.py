
from math import ceil


def h1(problema, s):
    """
    Heurística 1:
    Estima o custo restante considerando que
    o ferry transporta até 3 elementos por viagem.
    """

    mascara, barco = s

    # Identificar elementos ainda em Maputo
    restantes = []

    for i in range(problema.numero_elementos):

        esta_em_katembe = bool(mascara & (1 << i))

        if not esta_em_katembe:
            restantes.append(i)

    # Número mínimo de travessias estimado
    viagens = ceil(len(restantes) / 3)

    # Se o barco estiver em Maputo, considerar
    # pelo menos uma travessia para chegar a Katembe
    if barco == 0:
        viagens = max(viagens, 1)

    return 10 * viagens


def h2(problema, s):
    """
    Heurística 2:
    Considera a capacidade máxima de 3 elementos
    e a obrigação de transportar pelo menos um adulto.
    """

    mascara, barco = s

    restantes = []

    # Identificar elementos ainda em Maputo
    for i in range(problema.numero_elementos):

        esta_em_katembe = bool(mascara & (1 << i))

        if not esta_em_katembe:
            restantes.append(i)

    # Número total de elementos restantes
    total_restantes = len(restantes)

    # Identificar os elementos que não são adultos
    nao_adultos = [
        i for i in restantes
        if i not in (0, 1)
    ]

    total_nao_adultos = len(nao_adultos)

    # Limite inferior pelo número total de elementos
    viagens_total = ceil(total_restantes / 3)

    # Limite inferior pelo número de não adultos
    viagens_nao_adultos = ceil(total_nao_adultos / 2)

    # Escolher a estimativa mais elevada
    viagens = max(
        viagens_total,
        viagens_nao_adultos
    )

    # Considerar a posição do barco
    if barco == 0:
        viagens = max(viagens, 1)

    return 10 * viagens
