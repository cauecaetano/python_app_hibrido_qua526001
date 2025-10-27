# TODO: atividade 

# tratamento de exceção 
try:
    # entradad de dados 
    nome = input("Informe o nome: ").strip().title()
    peso = float(input("Infrome o peso em kg: ").strip().replace(",","."))
    altura = float(input("INfrome a altura em metros: ").strip().replace(",","."))

    # cálculo do IMC
    imc = peso/(altura**2)

    # exibe o imc do usuário 
    if imc < 18.5:
         print(f"{nome}, está baixo do peso")
    elif imc < 25:
            print(f"{nome} está no peso ideal.")
    elif imc < 30:
         print(f"{nome} está acima do peso.")
    elif imc < 35:
         print(f"{nome}está com obesidade nível 2.")
    else:
         print(f"{nome}está com obesidade mórbida.")
except Exception as e: 
    print(f"Deu ruim! {e}")