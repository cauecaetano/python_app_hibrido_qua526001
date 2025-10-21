# declaração de variáveis
x = float(input("informe o 1° número: ").strip().replace(",","."))
y = float (input("informe o 2° número: ").strip().replace(",","."))

# meu
print("1 - Soma")
print("2 - subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operador = input("informe a operação desejada: ").strip()

# decisão
match operador:
    case "1":
         print(f"A soma é{x+y}")
    case "2":
        print(f"A subtração é{x + y}")
    case "3":
        print(f"A multiplicaçãoé {x*y}")
    case "4":
        print(f"A divisão é {x/y}")
        print("Operação inválida.")