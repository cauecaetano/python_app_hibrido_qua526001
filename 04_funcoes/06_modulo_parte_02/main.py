# função principal 
def main():
    # entradas de dados 
    nome = input("Informe o seu nome: ").strip().title()
    idade = int(input("Infrome sua idade: ").strip())

    # operador ternário 
    resultado = " é maoir de idade." if idade >= 18 else " é menor de idade."

    # saída de dados 
    print(f"{nome} {resultado}")

# protege algoritimo principal 
if __name__ == "__main__":
    main()