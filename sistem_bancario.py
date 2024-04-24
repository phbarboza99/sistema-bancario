import os
menu= """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

Digite a opção que deseja """

saldo= 0
limite= 500 # Valor máximo que o usuário pode escolher por saque
extrato=[]
numero_saque=0
LIMITE_SAQUES=3 #Valor máximo que pode sacar

while True: 
    opcao = int(input(menu))

    match opcao:
        case 1:
            os.system('cls')
            print("Você está na área de depósito") 
            valor_deposito = float(input("Insira um valor para depósito: "))       
            if valor_deposito > 0:
                saldo += valor_deposito
                resumo_dep = f"Depósito de R${valor_deposito}"
                extrato.append(resumo_dep)
                print(f"Foi Depositado R${valor_deposito}")
            else:
                print("O valor precisa ser maior do que zero")

        case 2:
            os.system('cls')
            print("Você está na área de saque")
            if numero_saque < LIMITE_SAQUES:
                valor_saque= float(input("Insira o valor que deseja sacar: "))
                if valor_saque > 0:
                    if valor_saque <= limite:
                        if valor_saque <= saldo:
                            saldo = saldo - valor_saque
                            resumo_saque = f"Saque de R$ {valor_saque}"
                            extrato.append(resumo_saque)
                            print(f"Foi sacado R$ {valor_saque}")
                        else:
                            print("O valor que deseja sacar é inferior ao saldo.")
                    else:
                        print(f"O valor excede o limite de {limite}")
                else: 
                    print("O valor precisa ser maior que zero")
            else:
                print("Você já excedeu a quantidade máxima de saque por hoje, tenta novamente amanhã!")

        case 3:
            os.system('cls')
            print("Você está na área de extrato:")
            print("==========================")
            tamanho_extrato = len(extrato)
            if tamanho_extrato > 0:
                for item_lista in extrato:
                    print(f"Foi feito um {item_lista}")
            else:
                print("Não houve movimentações de deposito ou saque")
            print("==========================")
        
        case 4: 
            print("Saindo do Programa")
            break
                    