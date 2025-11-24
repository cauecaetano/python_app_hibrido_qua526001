import os 
from datetime import datetime

def limpar():
    os.system("cls" if os.name == "nt" else clear)

def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        genero = input("Informe o gênero: ").strip()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa)").strip()
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()
        email = input("Informe o e-mail: ").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email))

        if email in [pessoa.email for pessoa in pessoas]:
            return "E-mail já cadastrado."
        else:
            nova_pessoa = Pessoa(nome=nome, nascimento=nascimento, email=email, genero=genero)

            # insert into pessoa 
            session.add(nova_pessoa)
            session.commit()

            return "Pessoa {nova_pessoa.nome} cadastrar com sucesso."

    except Exception as e:
        print(f"Não foi posível cadastrar. {e}.")

# read
def listar(session, Pessoa):
    try: 
        pessoas = session.query(Pessoa).all()

        print("Pessoas cadastradas:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Gênero: {pessoa.genero}")
            print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
            print(f"\n{'-'*40}\n")
    except Exception as e:
        print(f"Não foi possível listar. {e}.")

# update
def atualizar(session, Pessoa):
    id_pessoa = ""
    email = ""
    novo_nome = ""
    novo_email =""
    novo_nascimento = ""
    novo_genero = ""

    try:
        print("Escolha o campo que deseja pesquisar: ")
        print("1 - ID")
        print("2 - E-mail ")
        print("3 -Retornar ")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe o e-mail: ").strip().lower()
                pessoa = session.query(Pessoa).filtery_by(email=email).first()
            case "3":
                return
            case _:
                return "Opção inválida."
                 
        if pessoa:
            limpar()
            while True:
                print(f"Qual campo deseja alterar:\n")
                print("Qual campo deseja alterar:\n")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
                print(f"4 - Gênero: {pessoa.genero}")
                print(f"5 - Finalizar")
                campo = input("Campo desejado: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome").strip().title()
                        continue
                    case "2":
                        novo_email = input("Informe o novo e-mail ").strip().lower()
                        pessoas = session.query(Pessoa)(Pessoa.email == novo_email).all()
                        if email in {pessoa.email for pessoa in pessoa}:
                            continue
                    case "3":
                        novo_nascimento = input("Informe q nova data de nascimento (dd/mm/aaa): ").strip()
                        continue
                    case "4":
                        novo_genero = input("Informe o novo gênero ").strip()
                        continue
                    case "5":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        novo_nascimento = datetime.strptime(novo_nascimento,"%d/%m/%Y").date() if novo_nascimento != "" else pessoa.nascimento
                        novo_genero = novo_genero if novo_genero != "" else pessoa.genero
                        break
                    case _:
                        print("Campo inexistente.")
                        continue
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero

            session.commit()

    except Exception as e:
        print(f"Não foi poddível alterar os dados. {e}.")

def deletar(session, Pessoa):
    id_pessoa = ""
    email = ""
    pessoa = ""

    print("Informe o campo que deseja")
    print("1 - ID")
    print("2 - E-mail")
    print("3 - Retornar")
    opcao = input("Informe o campo que deseja pesquisar: ").strip()
    limpar()
    match opcao:
        case "1":
            id_pessoa = input("Informe o ID ser excluído: ").strip()
            pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
        case "2":
            email = input("Informe o e-mail do cadastro a ser excluído: ").strip().lower()
            pessoa = session.query(Pessoa).filter_by(email=email).first()
        case "3":
            return 
        case _:
            return "Opção inválida."
    
    if pessoa:
        limpar()
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"E-mail: {pessoa.email}")
        print(f"Gênero: {pessoa.genero}")
        print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%y")}")
        print({'-'*40})
        print("1 - Sim")
        print("2 - Não")
        excluir = input("Tem certeza de que deseja excluir o registro? ").strip()
        match excluir:
            case "1":
                session.delete(pessoa)
                session.commit()
                return "Pessoa excluída com sucesso.🤓​"
            case "2":
                return ""
            case _:
                return "Opção inválida"