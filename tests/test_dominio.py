
import pytest

from dominio import ProblemaFerry


@pytest.fixture
def problema():
    return ProblemaFerry()


def test_estado_inicial(problema):
    """Verifica se o estado inicial está correcto."""
    assert problema.estado_inicial() == (0, 0)


def test_estado_objectivo(problema):
    """Verifica se o estado final é reconhecido."""
    estado_final = (511, 1)

    assert problema.e_objectivo(estado_final)


def test_ferry_transporta_adulto(problema):
    """Verifica se todas as acções geradas transportam um adulto."""
    estado = problema.estado_inicial()

    for accao in problema.accoes(estado):
        assert 0 in accao or 1 in accao


def test_ferry_nao_ultrapassa_tres_elementos(problema):
    """Verifica se uma acção com mais de três elementos é rejeitada."""
    estado = problema.estado_inicial()

    with pytest.raises(ValueError):
        problema.resultado(estado, (0, 2, 3, 4))


def test_ferry_nao_ultrapassa_150_kg(problema):
    """Verifica se uma carga superior a 150 kg é rejeitada."""
    estado = problema.estado_inicial()

    # A1 (75 kg) + A2 (70 kg) + C (30 kg) = 175 kg
    with pytest.raises(ValueError):
        problema.resultado(estado, (0, 1, 2))


def test_gas_e_combustivel_nao_viajam_juntos(problema):
    """Verifica a incompatibilidade entre gás e combustível."""
    estado = problema.estado_inicial()

    with pytest.raises(ValueError):
        problema.resultado(estado, (0, 7, 8))


def test_margens_permanecem_seguras(problema):
    """Verifica se as acções geradas mantêm as duas margens seguras."""
    estado = problema.estado_inicial()

    for accao in problema.accoes(estado):
        novo_estado = problema.resultado(estado, accao)
        mascara, _ = novo_estado

        assert problema.estado_seguro(mascara)


def test_accao_sem_adulto_e_rejeitada(problema):
    """Verifica se o ferry rejeita uma acção sem adulto."""
    estado = problema.estado_inicial()

    with pytest.raises(ValueError):
        problema.resultado(estado, (2,))



def test_accao_que_deixa_margem_insegura_e_rejeitada(problema):
    """Verifica se uma acção que deixa uma margem insegura é rejeitada."""

    estado = problema.estado_inicial()

    # 1. A1 e C atravessam para Katembe.
    estado = problema.resultado(estado, (0, 2))

    # 2. A1 regressa a Maputo, deixando C em Katembe.
    estado = problema.resultado(estado, (0,))

    # 3. A2 e o cão atravessam para Katembe.
    estado = problema.resultado(estado, (1, 6))

    # 4. A2 tenta regressar sozinho.
    # Isso deixaria C e o cão juntos, sem adulto em Katembe.
    with pytest.raises(ValueError):
        problema.resultado(estado, (1,))

def test_custo_da_travessia(problema):
    """Verifica a fórmula de custo de uma travessia."""
    estado = problema.estado_inicial()
    accao = (0,)  # A1 pesa 75 kg
    novo_estado = problema.resultado(estado, accao)

    custo = problema.custo(estado, accao, novo_estado)

    assert custo == 17.5
