from item import *

class ValidadorFerramenta:
    @staticmethod
    def validar_nome(nome):
        if not isinstance(nome, str):
            raise ValueError("O nome deve ser uma string.")

    @staticmethod
    def validar_codigo(codigo):
        if not isinstance(codigo, str):
            raise ValueError("O código deve ser uma string.")

    @staticmethod
    def validar_quantidade(quantidade):
        if not isinstance(quantidade, int) or quantidade < 0:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")

class Ferramenta(Item):
    def __init__(self, nome: str, codigo: str, quantidade: int):
        super().__init__(nome, codigo, quantidade)
        ValidadorFerramenta.validar_nome(nome)
        ValidadorFerramenta.validar_codigo(codigo)
        ValidadorFerramenta.validar_quantidade(quantidade)

    def get_detalhes(self):
        return "" #Ferramentas não tem detalhes adicionais neste quesito

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        ValidadorFerramenta.validar_nome(valor)
        self._nome = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        ValidadorFerramenta.validar_codigo(valor)
        self._codigo = valor

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, valor):
        ValidadorFerramenta.validar_quantidade(valor)
        self._quantidade = valor

    def __str__(self):
        return f"Ferramenta: {self.nome}, Código: {self.codigo}, Quantidade: {self.quantidade}"
