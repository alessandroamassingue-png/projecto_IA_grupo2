
import pytest

from dominio import ProblemaFerry
from buscas import busca_greedy


@pytest.mark.parametrize("heuristica", ["h1", "h2"])
def test_greedy_encontra_solucao(heuristica):
    problema = ProblemaFerry()

    percurso, expandidos, gerados = busca_greedy(
        problema,
        heuristica
    )

    assert percurso is not None
    assert problema.e_objectivo(percurso[-1].estado)

    assert expandidos > 0
    assert gerados > 0

    for i in range(1, len(percurso)):
        anterior = percurso[i - 1].estado
        no = percurso[i]

        assert problema.resultado(anterior, no.accao) == no.estado
