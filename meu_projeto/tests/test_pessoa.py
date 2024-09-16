import pytest
from datetime import date
from meu_projeto.models.enums.sexo import Sexo
from meu_projeto.models.enums.unidadeFederativa import UnidadeFederativa
from meu_projeto.models.endereco import Endereco
from meu_projeto.models.pessoa import Pessoa

# Modelo
@pytest.fixture
def test_criar_pessoa():
   pessoa = Pessoa(1, "João Silva", date(1990, 5, 21), "9999-9999", "joao.silva@email.com", Sexo.MASCULINO,
                Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Salvador", UnidadeFederativa.BAHIA))
   return pessoa

def test_pessoa_atributo_nome(criar_pessoa):
   assert criar_pessoa.nome == "João Silva"

def test_pessoa_atributo_data_nascimento(criar_pessoa):
    assert criar_pessoa.dataNascimento == date(1990, 5, 21)