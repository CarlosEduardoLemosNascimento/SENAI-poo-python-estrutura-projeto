class Endereco:
    def __init__(self,  logradouro:str, numero:int) -> None:
        self.logradouro = logradouro
        self.numero = numero

    def __str__(self) -> str:
        return(
                f"\nLogradouro: {self.logradouro}"
                f"\nNumero: {self.numero}"
                )
