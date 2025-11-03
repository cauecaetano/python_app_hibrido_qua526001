# biblioteca 
import os

# função 
def boas_vindas(nome):
    os.system("cls")
    return f"Seja bem vindo, {nome}! 😴"

# algoritmo primcipal 
os.system("cls")
nome = input("Informe seu nome: ").strip().title()
resultado = boas_vindas(nome)
print(resultado)