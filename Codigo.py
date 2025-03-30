class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso!')
        else:
            print('Saldo insuficiente ou valor inválido.')

    def transferir(self, valor, conta_destino):
        """Transfere um valor de uma conta para outra."""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f'Transferência de R${valor:.2f} para a conta {conta_destino.numero} realizada com sucesso!')
        else:
            print('Saldo insuficiente ou valor inválido para a transferência.')

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero, titular):
        if numero not in self.contas:
            conta = Conta(numero, titular)
            self.contas[numero] = conta
            print(f'Conta de {titular} criada com sucesso!')
        else:
            print('Conta com este número já existe.')

    def buscar_conta(self, numero):
        return self.contas.get(numero)

    def listar_contas(self):
        if not self.contas:
            print('Não há contas cadastradas.')
        else:
            print('Contas cadastradas:')
            for numero, conta in self.contas.items():
                print(f'Número: {numero}, Titular: {conta.titular}, Saldo: R${conta.saldo:.2f}')

def menu():
    banco = Banco()

    while True:
        print("\n-- Menu do Banco --")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Listar contas")
        print("5. Transferir")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            numero = input("Digite o número da conta: ")
            titular = input("Digite o nome do titular: ")
            banco.criar_conta(numero, titular)
