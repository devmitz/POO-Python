class Conta:

#Construtor
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

#Métodos
    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_sacar
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")
    def deposito(self, valor):
        self.__saldo += valor
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposito(valor)
        print("Transferência realizada com sucesso.")

    #Getters

    @property
    def numero(self):
        return self.__numero
    @property
    def titular(self):
        return self.__titular
    @property
    def saldo(self):
        return self.__saldo
    @property
    def limite(self):
        return self.__limite

    #Setters

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    #StaticMethods

    @staticmethod
    def codigo_banco():
        return "001"
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'} 