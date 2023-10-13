menu = """
Escolha a opção desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Informe a quantia a ser depositada: "))
        if deposito < 0:
            print("Não é possível realizar depositos negativos")
        else:
            saldo+=deposito
            print(f"Depósito realizado com sucesso, seu saldo agora é de: {saldo:.2f}")
            extrato+= f"Depósito: R$ {deposito:.2f}\n"
            

    elif opcao == "s":
        saque_desejado = int(input("Informe a quantidade a ser sacada: "))
        if saque_desejado <= 0:
            print("Não é possível realizar operação. Valor inválido")
        elif saque_desejado > limite:
            print(f"Não foi possível realizar a operação, saque excedeu o limite de {limite:.2f}")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Não foi possível realizar a operação, limite de número saques atingido ")
        elif saque_desejado > saldo:
            print(f"Não foi possível realizar a operação. Saldo insuficiente")
        else:
            saldo-=saque_desejado
            numero_saques+=1
            print(f"Saque realizado com sucesso. Seu saldo agora é de {saldo:.2f}")
            extrato+= f"Saque: R$ {saque_desejado:.2f}\n"

    elif opcao == "e":
        print("\n=========== Extrato ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")


    elif opcao == "q":
        break

    else: 
        print("Operação inválida, por favor seleciona novamente a operação desejada")