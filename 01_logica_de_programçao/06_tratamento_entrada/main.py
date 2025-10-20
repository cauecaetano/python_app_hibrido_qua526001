# declaração de vaiáveis # elimina espaço
nome = input("informe seu nome:").strip().title()#elimina os espaços antes e depois da variável
idade = int(input("informe sua idade: ").strip())
altura = float(input("infrome sua altura").replace(",","."))

# saida de dados 
print(f"nome do usuário: {nome}. Tipo: {type(nome)}")
print(f"idade: {idade}. Tipo: {type(idade)}")
print(f"altura: {altura} metros. tipo: {type(altura)}")