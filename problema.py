from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Hashable, Optional


class Problema(ABC):
    """
    Classe abstracta para representar problemas de pesquisa.
    """

    @abstractmethod
    def estado_inicial(self) -> Hashable:
        pass

    @abstractmethod
    def accoes(self, s: Hashable) -> list:
        pass

    @abstractmethod
    def resultado(self, s: Hashable, a: Any) -> Hashable:
        pass

    @abstractmethod
    def custo(self, s: Hashable, a: Any, s2: Hashable) -> float:
        pass

    @abstractmethod
    def e_objectivo(self, s: Hashable) -> bool:
        pass

    @abstractmethod
    def heuristica(self, s: Hashable, nome: str) -> float:
        pass


@dataclass
class No:

    estado: Hashable
    pai: Optional[No] = None
    accao: Any = None
    g: float = 0
    profundidade: int = 0


def caminho(no: No) -> list:

    percurso = []

    actual = no

    while actual is not None:
        percurso.append(actual)
        actual = actual.pai

    percurso.reverse()

    return percurso
