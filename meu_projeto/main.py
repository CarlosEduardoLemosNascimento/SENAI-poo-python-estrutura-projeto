import os

from datetime import date
from models.enums.sexo import Sexo
from models.enums.unidadeFederativa import UnidadeFederativa
from models.endereco import Endereco
from models.pessoa import Pessoa

os.system("cls || clear")


# Criando um endereço
endereco = Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA)

# Criando uma pessoa
pessoa = Pessoa(1, "João Silva", date(1990, 5, 21), "9999-9999", "joao.silva@email.com", Sexo.MASCULINO, endereco)

# Exibindo informações da pessoa
print(pessoa)
###