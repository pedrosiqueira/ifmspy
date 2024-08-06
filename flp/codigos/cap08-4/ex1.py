import pickle
from classes import Endereco, Pessoa


def salvar_objetos(objetos, arquivo):
    with open(arquivo, "wb") as file:
        pickle.dump(objetos, file)


def carregar_objetos(arquivo):
    try:
        with open(arquivo, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []


def adicionar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
    endereco = Endereco(
        input("Digite o logradouro: "), input("Digite o número: "), input("Digite o bairro: "), input("Digite o CEP: "), input("Digite a cidade: "), input("Digite o estado: ")
    )
    pessoa = Pessoa(nome, data_nascimento, endereco)
    pessoas.append(pessoa)
    print("Pessoa adicionada com sucesso.")


def excluir_pessoa():
    nome = input("Digite o nome da pessoa a ser excluída: ")
    for pessoa in pessoas:
        if pessoa.nome == nome:
            pessoas.remove(pessoa)
            print("Pessoa excluída com sucesso.")
            return
    print("Pessoa não encontrada.")


def listar_pessoas():
    print("\nLista de Pessoas:")
    for pessoa in pessoas:
        print(f"Nome: {pessoa.nome}, Data de Nascimento: {pessoa.data_nascimento}")
        print(
            f"Endereço: {pessoa.endereco.logradouro}, {pessoa.endereco.numero}, {pessoa.endereco.bairro}, {pessoa.endereco.cep}, {pessoa.endereco.cidade}, {pessoa.endereco.estado}"
        )
        print()


def menu():
    print("\n===== Menu =====")
    print("1. Adicionar Pessoa")
    print("2. Excluir Pessoa")
    print("3. Listar Pessoas")
    print("4. Encerrar")
    return input("Escolha uma opção: ")


pessoas = carregar_objetos("pessoas.pkl")

while True:
    opcao = menu()
    if opcao == "1":
        adicionar_pessoa()
    elif opcao == "2":
        excluir_pessoa()
    elif opcao == "3":
        listar_pessoas()
    elif opcao == "4":
        salvar_objetos(pessoas, "pessoas.pkl")
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
