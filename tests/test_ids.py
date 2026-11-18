
from dominio import ProblemaFerry
from buscas import busca_aprofundamento_iterativo


def test_ids_encontra_solucao_optima():
    problema = ProblemaFerry()

    (
        percurso,
        expandidos,
        gerados,
        reexpandidos,
        iteracoes
    ) = busca_aprofundamento_iterativo(
        problema,
        limite_maximo=50
    )

    assert percurso is not None
    assert problema.e_objectivo(percurso[-1].estado)
    assert len(percurso) - 1 == 9

    assert expandidos > 0
    assert gerados > 0
    assert reexpandidos >= 0
    assert iteracoes > 0

    for i in range(1, len(percurso)):
        anterior = percurso[i - 1].estado
        no = percurso[i]

        assert problema.resultado(anterior, no.accao) == no.estado
