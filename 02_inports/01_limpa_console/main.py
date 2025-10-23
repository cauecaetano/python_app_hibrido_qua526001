# importação de bibliotecas
import os 

# loop
while True:
    # limpeza de console 
    os.system("cls")

    #tratamento de exceção
    try:
        nome = input("Informe o nome: ").strip().title()
        email = input("Informe o e-mail: ").strip().lower()
        cpf = input("informe o CPF: ").strip()

        # limpeza de console 
        os.system("cls")

        # saída de dados 
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")

        # menu 
        print("1 - Inserir novos dados.")
        print("2 - Sair do programa.")
        opcao = input("Opção desejada: ").strip()

        # verificação a opção escolhida
        match opcao:
            case "1":
                continue 
            case "2":
                print("programador encerrado.")
                break
            case _:
                print("Opção inválida.")
                break
    except:
        print("Não foi possível receber informações.")