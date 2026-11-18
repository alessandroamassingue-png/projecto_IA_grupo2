
from dominio import ProblemaFerry

from buscas import (
    busca_bidireccional,
    busca_bidireccional_ucs
)


def test_bidireccional_bfs():
    problema = ProblemaFerry()

    percurso, expandidos, gerados = busca_bidireccional(problema)

    assert percurso is not None
    assert problema.e_objectivo(percurso[-1].estado)
    assert len(percurso) - 1 == 9

    assert expandidos > 0
    assert gerados > 0

    for i in range(1, len(percurso)):
        anterior = percurso[i - 1].estado
        no = percurso[i]

        assert problema.resultado(anterior, no.accao) == no.estado


def test_bidireccional_ucs():
    problema = ProblemaFerry()

    percurso, expandidos, gerados = busca_bidireccional_ucs(problema)

    assert percurso is not None
    assert problema.e_objectivo(percurso[-1].estado)
    assert len(percurso) - 1 == 9
    assert abs(percurso[-1].g - 180.0) < 0.000001

    assert expandidos > 0
    assert gerados > 0

    for i in range(1, len(percurso)):
        anterior = percurso[i - 1].estado
        no = percurso[i]

        assert problema.resultado(anterior, no.accao) == no.estado
