

class Conta:

    def __init__(self, numero, nome, valor):
        print("Constuindo o objeto....  {}".format(self))
        self.__numero = numero
        self.__titular = nome
        self.__saldo = valor
        self.__limite = 500.0
        self.__codigo_banco = "001"

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return "001"

    def __pode_sacar(self, valor):
        return valor <= (self.__saldo + self.__limite)


    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.__saldo, self.__titular))


    def deposita(self, valor):
        self.__saldo += valor


    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            return True

        print("Saldo insuficiente")
        return False


    def transfere(self, valor, destino):
        if self.saca(valor):
            destino.deposita(valor)
