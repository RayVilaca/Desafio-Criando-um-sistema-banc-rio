menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

extrato += f"Saldo inicial: R$ {saldo:.2f}\n\n"

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor a ser depositado:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            extrato += '.'*4 + f"Saldo: R$ {saldo:.2f}\n"
        else:
            print('Valor inválido. Tente novamente!')
    
    elif opcao == "s":
        valor = float(input("Insira o valor a ser sacado:"))
        
        if numero_saques == LIMITE_SAQUES:
            print("Número de saques diário excedido!")
        elif valor > limite:
            print(f"Valor máximo de R$ {limite:.2f} para saque excedido!")
        elif valor > saldo:
            print("Não será possível sacar o dinheiro por falta de saldo!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            extrato += '.'*4 + f"Saldo: R$ {saldo:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido. Tente novamente!")
    
    elif opcao == "e":
        print("."*30)
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato, end="")
            print('.'*30)
            print(f"Saldo atual: R$ {saldo:.2f}")
        print("."*30)
    elif opcao == "q":
        print("Programa finalizado ...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")