
import heapq
from math import inf

from dominio import ProblemaFerry


def obter_estados_alcancaveis(problema):
    """
    Descobre todos os estados que podem ser alcançados
    a partir do estado inicial.
    """
    inicial = problema.estado_inicial()

    visitados = {inicial}
    pilha = [inicial]

    while pilha:
        estado = pilha.pop()

        for accao in problema.accoes(estado):
            seguinte = problema.resultado(estado, accao)

            if seguinte not in visitados:
                visitados.add(seguinte)
                pilha.append(seguinte)

    return visitados


def calcular_custos_optimos(problema):
    """
    Calcula o custo óptimo de cada estado até ao objectivo,
    utilizando Dijkstra a partir do estado objectivo.

    Isto é válido porque as travessias deste problema
    são reversíveis e têm o mesmo custo nos dois sentidos.
    """
    objetivo = (problema.mascara_completa, 1)

    distancias = {objetivo: 0}
    fronteira = [(0, objetivo)]

    while fronteira:
        custo_atual, estado = heapq.heappop(fronteira)

        if custo_atual > distancias[estado]:
            continue

        for accao in problema.accoes(estado):
            anterior = problema.resultado(estado, accao)

            novo_custo = (
                custo_atual
                + problema.custo(estado, accao, anterior)
            )

            if novo_custo < distancias.get(anterior, inf):
                distancias[anterior] = novo_custo

                heapq.heappush(
                    fronteira,
                    (novo_custo, anterior)
                )

    return distancias


def verificar_reversibilidade(problema, estados):
    """
    Confirma se cada transição pode ser desfeita
    com a mesma acção e o mesmo custo.
    """
    for estado in estados:
        for accao in problema.accoes(estado):
            seguinte = problema.resultado(estado, accao)

            if accao not in problema.accoes(seguinte):
                return False

            reverso = problema.resultado(seguinte, accao)

            if reverso != estado:
                return False

            custo_ida = problema.custo(estado, accao, seguinte)
            custo_volta = problema.custo(seguinte, accao, estado)

            if custo_ida != custo_volta:
                return False

    return True


def testar_heuristicas():
    problema = ProblemaFerry()

    estados = obter_estados_alcancaveis(problema)
    custos_otimos = calcular_custos_optimos(problema)

    print("Número de estados alcançáveis:", len(estados))
    print("Número de estados com custo óptimo:", len(custos_otimos))

    # Confirmar se a reversibilidade é válida
    reversivel = verificar_reversibilidade(problema, estados)

    print("\n--- REVERSIBILIDADE ---")
    print("Transições reversíveis:", reversivel)

    if not reversivel:
        print("Não podemos usar Dijkstra a partir do objectivo desta forma.")
        return

    # Confirmar se todos os estados têm custo óptimo calculado
    if not estados.issubset(custos_otimos):
        print("ERRO: Existem estados sem custo óptimo calculado.")
        return

    violacoes_h1 = 0
    violacoes_h2 = 0
    violacoes_consistencia_h1 = 0
    violacoes_consistencia_h2 = 0
    violacoes_dominancia = 0

    for estado in estados:
        custo_otimo = custos_otimos[estado]

        valor_h1 = problema.heuristica(estado, "h1")
        valor_h2 = problema.heuristica(estado, "h2")

        # Teste de admissibilidade
        if valor_h1 > custo_otimo:
            violacoes_h1 += 1

        if valor_h2 > custo_otimo:
            violacoes_h2 += 1

        # Teste de dominância
        if valor_h2 < valor_h1:
            violacoes_dominancia += 1

        # Teste de consistência em cada transição
        for accao in problema.accoes(estado):
            seguinte = problema.resultado(estado, accao)
            custo = problema.custo(estado, accao, seguinte)

            h1_seguinte = problema.heuristica(seguinte, "h1")
            h2_seguinte = problema.heuristica(seguinte, "h2")

            if valor_h1 > custo + h1_seguinte:
                violacoes_consistencia_h1 += 1

            if valor_h2 > custo + h2_seguinte:
                violacoes_consistencia_h2 += 1

    print("\n--- ADMISSIBILIDADE ---")
    print("Violações de h1:", violacoes_h1)
    print("Violações de h2:", violacoes_h2)

    print("\n--- CONSISTÊNCIA ---")
    print("Violações de h1:", violacoes_consistencia_h1)
    print("Violações de h2:", violacoes_consistencia_h2)

    print("\n--- DOMINÂNCIA ---")
    print("Violações de h2 >= h1:", violacoes_dominancia)

    print("\n--- RESULTADO FINAL ---")

    assert reversivel, "Existem transições não reversíveis."

    assert estados.issubset(custos_otimos), (
        "Existem estados sem custo óptimo calculado."
    )

    assert violacoes_h1 == 0, "h1 não é admissível."
    assert violacoes_h2 == 0, "h2 não é admissível."

    assert violacoes_consistencia_h1 == 0, (
        "h1 não é consistente."
    )

    assert violacoes_consistencia_h2 == 0, (
        "h2 não é consistente."
    )

    assert violacoes_dominancia == 0, (
        "h2 não domina h1 em todos os estados."
    )

    print("Todos os testes foram aprovados!")

if __name__ == "__main__":
    testar_heuristicas()
