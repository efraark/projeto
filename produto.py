from interfaceItensServico import InterfaceItensServico

class Produto(InterfaceItensServico):
    def __init__(self, tipo, valor, quantidade):
        self.__tipo = tipo
        self.__valor = valor
        self.__quantidade = quantidade

    def informacaoServiço(self):
        return f"Produto utilizado\n{self.__tipo}\n\nQuantidade\n{self.__quantidade}\n\nValor total\n{self.__valor}"

    def getValorTotal(self):
        return self.__valor * self.__quantidade
    
    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, new_tipo):
        self.__tipo = new_tipo

    
    def setValor(self, new_valor):
        self.__valor = new_valor

    def getQuantidade(self):
        return self.__quantidade
    
    def setQuantidade(self, new_quantidade):
        self.__quantidade = new_quantidade

    def informacaoItem(self):
        # Melhorando a formatação da string para maior clareza
        return (f"Tipo: {self.__tipo}\n"
                f"Valor Unitário: {self.__valor}\n"
                f"Quantidade: {self.__quantidade}\n"
                f"Valor Total: {self.getValorTotal()}")