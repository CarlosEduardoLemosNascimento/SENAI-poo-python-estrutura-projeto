import os

from datetime import date
from meu_projeto.models.enums.sexo import Sexo
from meu_projeto.models.enums.unidadeFederativa import UnidadeFederativa
from meu_projeto.models.endereco import Endereco
from meu_projeto.models.pessoa import Pessoa

os.system("cls || clear")


# Criando um endereço
endereco = Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA)

# Criando uma pessoa
pessoa = Pessoa(1, "João Silva", date(1990, 5, 21), "9999-9999", "joao.silva@email.com", Sexo.MASCULINO, endereco)

# Exibindo informações da pessoa
print(pessoa)
###