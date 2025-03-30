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

    def consultar_saldo(self):
        print(f'O saldo da conta {self.numero} é R${self.saldo:.2f}.')

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
        print("4. Consultar saldo")
        print("5. Listar contas")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            numero = input("Digite o número da conta: ")
            titular = input("Digite o nome do titular: ")
            banco.criar_conta(numero, titular)

        elif escolha == '2':
            numero = input("Digite o número da conta: ")
            conta = banco.buscar_conta(numero)
            if conta:
                valor = float(input("Digite o valor a ser depositado: R$"))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif escolha == '3':
            numero = input("Digite o número da conta: ")
            conta = banco.buscar_conta(numero)
            if conta:
                valor = float(input("Digite o valor a ser sacado: R$"))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif escolha == '4':
            numero = input("Digite o número da conta: ")
            conta = banco.buscar_conta(numero)
            if conta:
                conta.consultar_saldo()
            else:
                print("Conta não encontrada.")

        elif escolha == '5':
            banco.listar_contas()

        elif escolha == '6':
            print("Saindo do banco...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
