import os

# Função para limpar o console
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dados do usuário 
nome = input("Informe seu nome: ")
email = input("Informe seu e-mail: ")
cpf = input("Informe seu CPF: ")
telefone = input("Informe seu telefone: ")

# importação de bibliotecas 
import os 
import time

while True:
    # Limpa o console
    limpar_console()

    # mensagens
    print("carregando...")
    time.sleep(7)

    print("processando informações...")
    time.sleep(7)

    print("Carregado")
    time.sleep(3)

    break

# Informação do usuário 
print(f"Nome: {nome} ")
print(f"E-mail: {email} ")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone} ")
