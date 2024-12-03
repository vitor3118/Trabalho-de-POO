import random
from datetime import datetime

class Conta:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        self.__saldo = 0.0
        self.logs = []

    def autenticar(self):
        tentativas = 3
        while tentativas > 0:
            senha = input("Digite sua senha: ")
            if senha == self.__senha:
                return True
            else:
                tentativas -= 1
                print(f"Senha incorreta. Você tem {tentativas} tentativa(s) restante(s).")
        print("Acesso bloqueado.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.registrar_log(f"Depósito de R$ {valor:.2f} realizado.")
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            self.registrar_log(f"Saque de R$ {valor:.2f} realizado.")
            print(f"Saque de R$ {valor:.2f} realizado.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")
        self.registrar_log("Consulta de saldo.")

    def registrar_log(self, operacao):
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.logs.append(f"[{timestamp}] {operacao}")

    def mostrar_logs(self):
        print("Histórico de Operações:")
        for log in self.logs:
            print(log)

    def get_saldo(self):
        return self.__saldo


class ContaPoupanca(Conta):
    def __init__(self, nome, senha):
        super().__init__(nome, senha)
        self.__aplicado = 0.0

    def aplicar(self, valor):
        saldo_atual = self.get_saldo()
        if valor > 0 and valor <= saldo_atual:
            self.__aplicado += valor
            self.depositar(-valor)
            self.registrar_log(f"Aplicação de R$ {valor:.2f} realizada.")
            print(f"Aplicação de R$ {valor:.2f} realizada.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def resgatar(self, valor):
        if valor > 0 and valor <= self.__aplicado:
            self.__aplicado -= valor
            self.depositar(valor)
            self.registrar_log(f"Resgate de R$ {valor:.2f} realizado.")
            print(f"Resgate de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_aplicado(self):
        print(f"Saldo aplicado: R$ {self.__aplicado:.2f}")
        self.registrar_log("Consulta de saldo aplicado.")


def criar_conta():
    nome = input("Informe seu nome: ")
    senha = input("Crie uma senha de 4 dígitos: ")
    while len(senha) != 4:
        print("A senha deve ter exatamente 4 dígitos.")
        senha = input("Crie uma senha de 4 dígitos: ")
    print(f"Conta criada para {nome}.")
    return ContaPoupanca(nome, senha)


def menu_principal(conta):
    while True:
        print(f"\nBem-vindo ao Banco MAIS, {conta._Conta__nome}!")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar Saldo")
        print("4 - Poupança")
        print("5 - Ver Logs")
        print("6 - Sair")
        try:
            opcao = int(input("Escolha uma operação: "))
            if opcao == 1:
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
            elif opcao == 2:
                if conta.autenticar():
                    valor = float(input("Valor do saque: "))
                    conta.sacar(valor)
            elif opcao == 3:
                conta.consultar_saldo()
            elif opcao == 4:
                menu_poupanca(conta)
            elif opcao == 5:
                conta.mostrar_logs()
            elif opcao == 6:
                print("Obrigado por usar o Banco MAIS!")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida.")


def menu_poupanca(conta):
    while True:
        print("\n1 - Aplicar")
        print("2 - Resgatar")
        print("3 - Consultar")
        print("4 - Voltar")
        try:
            opcao = int(input("Escolha uma operação: "))
            if opcao == 1:
                valor = float(input("Valor a aplicar: "))
                conta.aplicar(valor)
            elif opcao == 2:
                valor = float(input("Valor a resgatar: "))
                conta.resgatar(valor)
            elif opcao == 3:
                conta.consultar_aplicado()
            elif opcao == 4:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida.")


# Execução do Programa
conta_criada = criar_conta()
menu_principal(conta_criada)