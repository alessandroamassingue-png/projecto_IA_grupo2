
from itertools import combinations

from problema import Problema


class ProblemaFerry(Problema):
    """
    Representa o problema da travessia do ferry
    entre Maputo e Katembe.

    Estado:
        (mascara, barco)

        mascara:
            Representa a localização dos elementos.
            0 = Maputo
            1 = Katembe

        barco:
            0 = Maputo
            1 = Katembe
    """

    def __init__(self, estado_inicial=(0, 0)):
        """
        Inicializa o problema do ferry.

        O estado inicial pode ser personalizado.
        O estado objectivo continua a ser (511, 1).
        """

        # Identificação dos elementos.
        self.nomes = [
            "A1", "A2", "C", "Cabrito", "Milho",
            "Galinhas", "Cao", "Gas", "Combustivel"
        ]

        # Peso de cada elemento em quilogramas.
        self.pesos = [
            75, 70, 30, 40, 50,
            10, 25, 15, 25
        ]

        self.numero_elementos = len(self.nomes)

        # Máscara com todos os elementos.
        self.mascara_completa = (
                (1 << self.numero_elementos) - 1
        )

        # Pares de elementos incompatíveis.
        self.incompativeis = [
            (2, 6),  # Criança e cão
            (2, 8),  # Criança e combustível
            (3, 4),  # Cabrito e milho
            (6, 5),  # Cão e galinhas
            (6, 3)  # Cão e cabrito
        ]

        # Estado objectivo fixo.
        self._estado_objectivo = (
            self.mascara_completa, 1
        )

        # Validar o estado inicial recebido.
        if (
                not isinstance(estado_inicial, tuple)
                or len(estado_inicial) != 2
        ):
            raise ValueError(
                "O estado inicial deve ser uma tupla (mascara, barco)."
            )

        mascara, barco = estado_inicial

        if type(mascara) is not int or type(barco) is not int:
            raise ValueError(
                "A máscara e a posição do barco devem ser inteiros."
            )

        if mascara < 0 or mascara > self.mascara_completa:
            raise ValueError("Máscara do estado inicial inválida.")

        if barco not in (0, 1):
            raise ValueError("A posição do barco deve ser 0 ou 1.")

        # Verificar se as duas margens são seguras.
        if not self.estado_seguro(mascara):
            raise ValueError(
                "O estado inicial apresenta uma margem insegura."
            )

        self._estado_inicial = estado_inicial

    def estado_inicial(self):
        """Devolve o estado inicial configurado."""
        return self._estado_inicial

    def e_objectivo(self, s):
        """Verifica se todos os elementos chegaram a Katembe."""

        mascara, barco = s

        return (
            mascara == self.mascara_completa
            and barco == 1
        )

    def margem_segura(self, mascara, margem_katembe):
        """
        Verifica se uma das margens é segura.

        Uma margem é segura quando:
        - Tem pelo menos um adulto; ou
        - Não contém pares incompatíveis.
        """

        elementos = []

        for i in range(self.numero_elementos):

            esta_em_katembe = bool(mascara & (1 << i))

            if esta_em_katembe == margem_katembe:
                elementos.append(i)

        # Verificar se existe um adulto na margem.
        tem_adulto = 0 in elementos or 1 in elementos

        if tem_adulto:
            return True

        # Verificar os pares incompatíveis.
        for a, b in self.incompativeis:

            if a in elementos and b in elementos:
                return False

        return True

    def estado_seguro(self, mascara):
        """Verifica a segurança das duas margens."""

        return (
            self.margem_segura(mascara, True)
            and self.margem_segura(mascara, False)
        )

    def accoes(self, s):
        """
        Devolve todas as acções válidas no estado actual.

        Cada acção transporta:
        - Pelo menos um adulto;
        - No máximo três elementos;
        - Até 150 kg.
        """

        mascara, barco = s

        disponiveis = []

        # Identificar os elementos que estão na margem do barco.
        for i in range(self.numero_elementos):

            esta_em_katembe = bool(mascara & (1 << i))

            if esta_em_katembe == bool(barco):
                disponiveis.append(i)

        accoes_validas = []

        # Gerar grupos com 1, 2 ou 3 elementos.
        for quantidade in range(1, 4):

            for grupo in combinations(disponiveis, quantidade):

                # É obrigatório transportar um adulto.
                if 0 not in grupo and 1 not in grupo:
                    continue

                peso = sum(self.pesos[i] for i in grupo)

                # Verificar o peso máximo.
                if peso > 150:
                    continue

                # Gás e combustível não podem viajar juntos.
                if 7 in grupo and 8 in grupo:
                    continue

                # Calcular a nova localização dos elementos.
                nova_mascara = mascara

                for i in grupo:
                    nova_mascara ^= (1 << i)

                # Verificar a segurança das margens.
                if not self.estado_seguro(nova_mascara):
                    continue

                accoes_validas.append(grupo)

        return accoes_validas

    def resultado(self, s, a):
        """
        Aplica uma acção e devolve o novo estado.

        Lança ValueError quando a acção é inválida.
        """

        mascara, barco = s

        # Verificar se a acção é uma tupla não vazia.
        if not isinstance(a, tuple) or not a:
            raise ValueError("Acção inválida neste estado.")

        # Verificar quantidade e elementos repetidos.
        if len(a) > 3 or len(set(a)) != len(a):
            raise ValueError("Acção inválida neste estado.")

        # Verificar se os elementos existem e estão
        # na mesma margem que o barco.
        for i in a:

            if (
                not isinstance(i, int)
                or i < 0
                or i >= self.numero_elementos
            ):
                raise ValueError("Elemento inválido na acção.")

            esta_em_katembe = bool(mascara & (1 << i))

            if esta_em_katembe != bool(barco):
                raise ValueError(
                    "Elemento não está na margem do barco."
                )

        # Verificar a presença de pelo menos um adulto.
        if 0 not in a and 1 not in a:
            raise ValueError(
                "O ferry precisa de transportar um adulto."
            )

        # Verificar o peso máximo.
        peso = sum(self.pesos[i] for i in a)

        if peso > 150:
            raise ValueError(
                "O peso máximo do ferry foi ultrapassado."
            )

        # Verificar a incompatibilidade entre gás e combustível.
        if 7 in a and 8 in a:
            raise ValueError(
                "Gás e combustível não podem viajar juntos."
            )

        # Aplicar a acção à máscara.
        nova_mascara = mascara

        for i in a:
            nova_mascara ^= (1 << i)

        # Verificar se as duas margens continuam seguras.
        if not self.estado_seguro(nova_mascara):
            raise ValueError(
                "A acção deixa uma margem insegura."
            )

        # Mudar a posição do barco.
        novo_barco = 1 - barco

        return (nova_mascara, novo_barco)

    def custo(self, s, a, s2):
        """
        Calcula o custo de uma travessia.

        Fórmula:
            Custo = 10 + Peso / 10
        """

        peso = sum(self.pesos[i] for i in a)

        return 10 + peso / 10

    def heuristica(self, s, nome):
        """Devolve a heurística solicitada."""

        if nome == "h0":
            return 0

        from heuristicas import h1, h2

        if nome == "h1":
            return h1(self, s)

        if nome == "h2":
            return h2(self, s)

        raise ValueError(
            f"Heurística desconhecida: {nome}"
        )

    def predecessores(self, s):
        """
        Devolve os estados que podem originar
        o estado actual.

        As travessias são reversíveis, pelo que
        podemos utilizar as mesmas acções e o
        modelo de transição existente.
        """

        anteriores = []

        for accao in self.accoes(s):

            estado_anterior = self.resultado(s, accao)

            anteriores.append(
                (estado_anterior, accao)
            )

        return anteriores
