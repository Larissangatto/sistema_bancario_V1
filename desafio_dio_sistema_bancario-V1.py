# importando bibliotecas
import datetime
import time

#criando o menu inicial
print("""\nOlá Usuário do Banco XX:
Por favor digitar a operação que você deseja realizar. No menu inicial \n\n""")

menu_inicial = """
................. Menu Inicial...............
[d] Depositar
[s] Sacar
[e] Exibir extrato
[q] Sair
...................................................
"""
# iniciando variaveis da conta do cliente
saldo = 0
LIMITE_SAQUE = 500
extrato  = ""
numero_saques = 0
LIMITE_SAQUES = 3
# código sem considerar operações mecanicas.
while True:
    opcao =  input(menu_inicial)

    if opcao == "d":
        print("\n-Você digitou acessou a função:\n- Depósito.\n")
        deposito = input("\nDigite o valor do depósito: R$ ")
        try:
            deposito = int(deposito)
            if deposito >=0:
                data = datetime.datetime.now()
                print(f"\n - O valor a ser depositado é : R$ {int(deposito)}.00.\n\n-Insira o dinheiro no local indicado pelo caixa com o símbolo $.\n")
                saldo = saldo + deposito
                extrato = extrato + (f"-Deposito: R${deposito},00 as {data.strftime('%H:%M - %d.%m.%Y')}\n")
                time.sleep(3)
                print(f"\n***-Depósito: R$ {deposito}.00 efetuado com sucesso as {data.strftime('%H:%M - %d.%m.%Y')}!")
                print("\n\n-Você será direcionado ao menu inicial!\n")
                time.sleep(2)
        except:
            print("\n###-Falha na operação: O caixa só aceita valores inteiros.")
            print("\n-Você será direcionado ao menu inicial.\n")
            time.sleep(2)   
        
          
    elif opcao == "s":
        print("\n-Você digitou acessou a função:\n- Saque.\n")
        saque = input("\nDigite o valor que deseja sacar: R$ ")
        try:
            saque = int(saque)
            if saque > saldo:
                print("\n###-Falha da operação: Saldo insuficiente!")
                print("\n\n-Você será direcionado ao menu inicial!\n")
                time.sleep(2)
            elif numero_saques >= LIMITE_SAQUES: 
                print("\n###-Falha da operação: Numero de saques diário já foi atingido.")
                print("\n\n-Você será direcionado ao menu inicial!\n")
                time.sleep(2)
            elif saque > LIMITE_SAQUE:
                print("\n###-Falha da operação: O Valor limite para cada saque é de R$ 500,00.")
                print("\n\n-Você será direcionado ao menu inicial!\n")
                time.sleep(2)
            elif saque >= 0:
                data = datetime.datetime.now()
                print(f"\n- O valor a ser sacado é : R$ {int(saque)},00.\n\n-Retire o dinheiro no local indicado pelo caixa com o símbolo $.\n")
                numero_saques += 1
                time.sleep(3)
                print(f"\n***-Saque de R$ {saque}.00 efetuado com sucesso as {data.strftime('%H:%M - %d.%m.%Y')}")
                print("\n\n-Você será direcionado ao menu inicial!\n")
                time.sleep(2)
                saldo = saldo - saque
                extrato = extrato + (f"Saque: R${saque}.00 as {data.strftime('%H:%M - %d.%m.%Y')} \n")
        except:
            print("\n###-Falha da operação: O caixa não possui moedas e só aceita valores inteiros.")
            print("\n\n-Você será direcionado ao menu inicial.\n")
            time.sleep(2)
    
    elif opcao == "e":
        data = datetime.datetime.now()     
        if extrato == "":
            print(f"=========================Extrato==========================\n\n-Você  não realizou nenhuma trasação hoje {data.strftime('%d.%m.%Y')}\n  Seu saldo atual é de R$ {saldo}.00!\n================================================================== \n\n-Você será direcionado ao menu inicial! \n")
        else:
            print(f"=========================Extrato==========================\n\n-Você realizou as seguintes operações:\n{extrato}\n  Seu saldo atual é R$ {saldo}.00 as {data.strftime('%H:%M - %d.%m.%Y')}!\n=========================================================== \n\n-Você será direcionado ao menu inicial!\n")
    
    elif opcao =="q":
        print("***Obrigado por utilizar nosso serviço eletrônico.\n")
        break

    else:
        print("### - Operação inválida, por favor selecione a operação desejada no menu inicial!\n")