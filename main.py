
class Conta():
    def __init__(self):
        self.saldo = 0
        self.extrato = []    
        self.quant_saques = 0
    
    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"\nDepósito efetuado no valor de R$ {valor:.2f}")
        print(f"O saldo atual é R$ {self.saldo:.2f}")
    
    def saque(self, valor):
        if self.quant_saques < 3:
            if valor <= 500 and valor > 0:
                if self.saldo - valor > 0:
                    self.saldo -= valor
                    self.extrato.append(f"Saque: R$ -{valor:.2f}")
                    self.quant_saques += 1
                    print(f"Saque efetuado no valor de R$ {valor:.2f}")
                    print(f"O saldo atual é R$ {self.saldo:.2f}")
                else: print("Você não tem saldo suficiente para esta operação.")
            else: print("O valor do saque deve ser maior do que 0 e menor ou igual a 500.")
        else: print("Você excedeu o limite de 3 saques.")

    def mostra_extrato(self):
        if self.extrato:
            print("\n---Extrato---")
            for i in self.extrato:
                print(i)
            print("---Fim---\n")
        else: print("\nSem movimentação.")
    
    def mostra_saldo(self):
        print("---Saldo---")
        print(f"R$ {self.saldo:.2f}")

conta = Conta()

while True:
    print("\ndigite:\n1 para depósitos\n2 para saques\n3 para mostrar o extrato\n4 para mostrar o saldo\n5 para sair\n")
    try:
        escolha = int(input("Escolha uma opção!\n"))
    except:
        print("Opção inválida")
        continue
    if escolha == 1:
        try:
            valor = round(float(input("Digite o valor do depósito\n")),2 )
            conta.deposito(valor)
        except:
            print("Valor inválido. Operação cancelada!")
    elif escolha == 2:
        try:
            valor = round(float(input("Digite o valor do saque\n")),2 )
            conta.saque(valor)
        except:
            print("Valor inválido. Operação cancelada!")
    elif escolha == 3:
        conta.mostra_extrato()
    elif escolha == 4:
        conta.mostra_saldo()
    elif escolha == 5:
        break
    else: print("Opção inválida.")