
import pytest

from dominio import ProblemaFerry
from buscas import busca_a_estrela


@pytest.mark.parametrize("heuristica", ["h1", "h2"])
def test_a_estrela_encontra_custo_optimo(heuristica):
    problema = ProblemaFerry()

    percurso, expandidos, gerados = busca_a_estrela(
        problema,
        heuristica
    )

    assert percurso is not None
    assert problema.e_objectivo(percurso[-1].estado)
    assert abs(percurso[-1].g - 180.0) < 0.000001

    assert expandidos > 0
    assert gerados > 0

    for i in range(1, len(percurso)):
        anterior = percurso[i - 1].estado
        no = percurso[i]

        assert problema.resultado(anterior, no.accao) == no.estado
