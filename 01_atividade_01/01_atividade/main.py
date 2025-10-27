# Números inteiros 
import time
import os

# Entradas de dados 
numero = int(input("Informe um número interessado: ").strip())

# loop, laço de repetição 
while numero >= 0:
    os.system("cls")
    print(f"{numero}")
    time.sleep(1)
    numero -= 1 

print("programa encerrado")