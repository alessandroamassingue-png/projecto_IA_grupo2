
import heapq
import pytest

from dominio import ProblemaFerry
from heuristicas import h1, h2


@pytest.fixture(scope="module")
def dados_validacao():
    """
    Calcula os estados alcançáveis e os custos óptimos
    restantes até ao estado objectivo, usando Dijkstra.
    """
    problema = ProblemaFerry()
    inicial = problema.estado_inicial()

    # 1. Descobrir todos os estados alcançáveis.
    estados = {inicial}
    fila = [inicial]

    while fila:
        estado = fila.pop(0)

        for accao in problema.accoes(estado):
            sucessor = problema.resultado(estado, accao)

            if sucessor not in estados:
                estados.add(sucessor)
                fila.append(sucessor)

    # 2. Encontrar o estado objectivo.
    objectivo = next(
        estado for estado in estados
        if problema.e_objectivo(estado)
    )

    # 3. Calcular os custos óptimos até ao objectivo.
    distancias = {objectivo: 0}
    fila_prioridade = [(0, objectivo)]

    while fila_prioridade:
        custo_actual, estado = heapq.heappop(fila_prioridade)

        if custo_actual > distancias[estado]:
            continue

        for anterior, accao in problema.predecessores(estado):
            custo = problema.custo(anterior, accao, estado)
            novo_custo = custo_actual + custo

            if novo_custo < distancias.get(anterior, float("inf")):
                distancias[anterior] = novo_custo

                heapq.heappush(
                    fila_prioridade,
                    (novo_custo, anterior)
                )

    return problema, estados, distancias, objectivo


def test_todos_estados_alcancaveis_tem_distancia(dados_validacao):
    """Verifica se todos os estados alcançáveis têm custo óptimo calculado."""
    _, estados, distancias, _ = dados_validacao

    assert len(estados) > 0
    assert estados == set(distancias)


def test_h1_e_admissivel(dados_validacao):
    """Verifica se h1 nunca ultrapassa o custo óptimo restante."""
    problema, estados, distancias, _ = dados_validacao

    for estado in estados:
        assert h1(problema, estado) <= distancias[estado]


def test_h2_e_admissivel(dados_validacao):
    """Verifica se h2 nunca ultrapassa o custo óptimo restante."""
    problema, estados, distancias, _ = dados_validacao

    for estado in estados:
        assert h2(problema, estado) <= distancias[estado]


def test_h1_e_consistente(dados_validacao):
    """Verifica a consistência de h1 em todas as transições."""
    problema, estados, _, _ = dados_validacao

    for estado in estados:
        for accao in problema.accoes(estado):
            sucessor = problema.resultado(estado, accao)
            custo = problema.custo(estado, accao, sucessor)

            assert h1(problema, estado) <= (
                custo + h1(problema, sucessor)
            )


def test_h2_e_consistente(dados_validacao):
    """Verifica a consistência de h2 em todas as transições."""
    problema, estados, _, _ = dados_validacao

    for estado in estados:
        for accao in problema.accoes(estado):
            sucessor = problema.resultado(estado, accao)
            custo = problema.custo(estado, accao, sucessor)

            assert h2(problema, estado) <= (
                custo + h2(problema, sucessor)
            )


def test_h2_domina_h1(dados_validacao):
    """Verifica se h2 é sempre maior ou igual a h1."""
    problema, estados, _, _ = dados_validacao

    for estado in estados:
        assert h2(problema, estado) >= h1(problema, estado)


def test_heuristicas_sao_zero_no_objectivo(dados_validacao):
    """Verifica se ambas as heurísticas valem zero no objectivo."""
    problema, _, _, objectivo = dados_validacao

    assert h1(problema, objectivo) == 0
    assert h2(problema, objectivo) == 0
