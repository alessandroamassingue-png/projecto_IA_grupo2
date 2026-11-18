
from dominio import ProblemaFerry
from buscas import busca_largura


def test_bfs_encontra_solucao():
    """Verifica se a BFS encontra uma solução válida."""

    problema = ProblemaFerry()

    percurso, expandidos, gerados = busca_largura(problema)

    # Verificar se foi encontrada uma solução.
    assert percurso is not None

    # Verificar se o estado final é o objectivo.
    assert problema.e_objectivo(percurso[-1].estado)

    # Verificar o número mínimo de travessias.
    assert len(percurso) - 1 == 9

    # Verificar se os contadores são válidos.
    assert expandidos > 0
    assert gerados > 0

    # Verificar todas as transições.
    for i in range(1, len(percurso)):
        no = percurso[i]
        estado_anterior = percurso[i - 1].estado

        estado_calculado = problema.resultado(
            estado_anterior,
            no.accao
        )

        assert estado_calculado == no.estado
