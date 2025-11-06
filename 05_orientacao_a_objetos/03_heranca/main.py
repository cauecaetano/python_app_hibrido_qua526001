# bibliotecas
import os 

# nossa biblioteca 
from classes import PessoaFisica, PessoaJuridica 

# função limpar tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# função principal 
def main():
    usuario = PessoaFisica(nome="", cpf="", idade=0, email="", telefone="")
    empresa = PessoaJuridica(nome_fantasia="", cnpj="", email="", telefone="")

    limpar()
    while True:
        print("1 - Inserir dados do usuário")
        print("2 - Inserir dados do empresa")
        print("3 - Inserir dados do usuário")
        print("4 - Inserir dados do empresa")
        print("5 - Inserir dados do programa")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                usuario.nome = input("Informe seu nome: ").strip().title()
                usuario.nome = input("Informe seu CPF: ").strip()
                usuario.nome = int(input("Informe seu idade: ").strip())
                usuario.nome = input("Informe seu e-mail: ").strip().lower()
                usuario.nome = input("Informe seu telefone: ").strip()
                limpar()
                continue 
            case "2":
                empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
                empresa.cnpj = input("Informe o CNPJ: ").strip()
                empresa.email = input("Informe o e-mail da empresa:" ).strip().lower()
                empresa.telefone = input("Informe o talefone da empresa: ").strip()
                limpar()
                continue 
            case "3":
                pass
            case "4":
                pass
            case "5":
                limpar()
                print("Programa encerrado. ")
                break
            case _:
                print("Programa inválida.")
                continue 

if __name__ == "__main__":
    main()