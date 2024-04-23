# Minha Resolução.

depositos=[]
saques=[]

opcao = 0
contSaque = 0

while opcao != 5:
    opcao=input('''O que você deseja realizar?
        1 - Depósito.
        2 - Saldo.
        3 - Saque.
        4 - Extrato.
        5 - Finalizar.
        
        Digite o número da opção desejada: ''')

    if opcao == "1":
        deposito = int(input('Qual o valor que deseja depositar em R$: '))
        depositos.append(deposito)  
        print(f'Foram adicionados R$ {deposito:.2f} em seu saldo bancário.')
    elif opcao == "2":
        extDep = sum(depositos)
        extSaq = sum(saques)
        saldoFin = extDep - extSaq
        print(f'O seu saldo atual é de R$ {saldoFin:.2f}')
    elif opcao == "3":
        if contSaque <= 2:
            saque=int(input('Digite o valor que você deseja sacar: '))
            if saque >= 501:
                print('Seu limite de saque é de R$ 500,00')
            else:
                saques.append(saque)
                saldoAtual = saldoFin - saque
                saldo = saldoAtual
                if saldo <= 0:
                    print('Seu saldo é insuficiente para realizar um saque desse valor.')
                else:
                    print(f'Seu saldo atual é de {saldoAtual:.2f}')
                    contSaque += 1
        else:
            print('Você ultrapassou seu limite diário de 3 saques!')
    elif opcao == "4":
        extrato = depositos
        extDep = sum(depositos)
        extSaq = sum(saques)
        extTotal = extDep - extSaq
        print(f'''Seu extrato de depósitos é: {depositos}.
                  O seu extrato de saque é: {saques}.
                  O seu saldo atual é de: R$ {extTotal}''')
    else:
        opcao = 5









