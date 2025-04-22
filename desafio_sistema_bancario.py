menu = '''

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        valor_do_deposito = float(input('Digite o valor do depósito: '))
        if valor_do_deposito >= 1:
            saldo += valor_do_deposito
            extrato += f'Depósito: R$ {valor_do_deposito:.2f}\n'
            print('Depósito realizado com sucesso.')
        else:
            print('Não foi possível realizar esse depósito. Por favor, digite um valor válido.')


    elif opcao == '2':
        valor = float(input('Digite o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Não foi possível realizar esse saque. Você não tem saldo suficiente.')
        elif excedeu_limite:
            print(f'Não foi possível realizar esse saque. O valor excede o limite de R${limite:.2f}.')
        elif excedeu_saques:
            print('Não foi possível realizar esse saque. Excedido o Número máximo de saques.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print('Saque realizado com sucesso.')

        else:
            print('Não foi possível realizar esse saque. O valor informado é inválido.')


    elif opcao == '3':
        print('\n================ EXTRATO ================')
        print('Nào foram realizados movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('==========================================')

    elif opcao == '0':
        print('Agradecemos por utilizar nosso sistema. Volte sempre e tenha um excelente dia!')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
