from abc import abstractmethod

class Item:
    def __init__(self, nome: str, codigo: str, quantidade: int):
        self.nome = nome
        self.codigo = f"{self.nome[:3].upper()}-{codigo}"
        self.quantidade = quantidade

    @abstractmethod
    def get_detalhes(self): #Retorna uma string com os detalhes específicos do item.
        pass