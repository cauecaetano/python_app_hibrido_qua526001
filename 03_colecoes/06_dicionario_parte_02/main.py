# declaração de dicionário
usuario = {
    'nome': "Cauê Caetano",
    'nascimento': "12/09/25",
    'email': "caue.caetano.santos@gmail.com",
    'telefone': "(61) 99377-2082",
    'endereço': "QI"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")