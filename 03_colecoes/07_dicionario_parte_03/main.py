# declaração de dicionário 
veiculo = {
    'fabricante': "Chevrolet",
    'modelo': "Chevette",
    'ano': 1973,
    'cor': "branco",
    'placa': "DF-1973"
}

# exibe os dados 
for chave in veiculo:
    print(f"{chave.capitalize()}:{veiculo[chave]}")

    # usuário escolhe o campo que deseja mudar
    while True:
        campo = input("Informe o nome do campo que deseja alterar ou digite 'sair para encerrar o programa: ").strip().lower()

        match campo:
            case "fabricante":
                veiculo['fabricante'] = input("Informe o novo valor de 'fabricante'").strip()
                continue
            case "modelo":
                veiculo['modelo'] = int(input("Informe o novo valor de 'modelo'").strip())
                continue
            case "ano":
                veiculo['modelo'] = input("Informe o novo valor de 'ano'").strip()
                continue
            case "cor":
                 veiculo['modelo'] = input("Informe o novo valor de 'cor'").strip()
                 continue
            case "placa":
                veiculo['modelo'] = input("Informe o novo valor de 'placa'").strip()
                continue
            case "sair":
                break
            case _:
                print("Valor inválido.")
                continue
    # mostra na tela novos valores
    for chave in veiculo:
        print(f"{chave.capitalize()}: {veiculo[chave]}")