from meu_projeto.models.enums.sexo import Sexo
from meu_projeto.models.endereco import Endereco

from datetime import date


class Pessoa:
    def __init__(self, id: int, nome: str, dataNascimento: date, telefone: str, email: str, sexo: Sexo, endereco: Endereco):
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Data de Nascimento: {self.dataNascimento}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"Sexo: {self.sexo.texto}\n"
                f"Sexo: {self.sexo.caractere}\n"
                #f"Sexo: {self.sexo.}\n"
                f"Endereço: {self.endereco}")