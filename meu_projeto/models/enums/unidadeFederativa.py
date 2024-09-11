from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")

    def __init__(self, nome: str, sigla: str):
        self.nome = nome
        self.sigla = sigla

    def __str__(self):
        return f"{self.nome} ({self.sigla})"
