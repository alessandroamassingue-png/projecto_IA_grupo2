
from dominio import ProblemaFerry
from buscas import busca_profundidade


def test_dfs_encontra_solucao():
    problema = ProblemaFerry()

    percurso, expandidos, gerados = busca_profundidade(
        problema,
        limite_profundidade=50
    )

    assert percurso is not None
    assert problema.e_objectivo(percurso[-1].estado)
    assert len(percurso) - 1 <= 50
    assert expandidos > 0
    assert gerados > 0

    for i in range(1, len(percurso)):
        anterior = percurso[i - 1].estado
        no = percurso[i]

        assert problema.resultado(anterior, no.accao) == no.estado
