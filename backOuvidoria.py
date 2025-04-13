"""
    Sistema de Ouvidoria 
    Autor: Otávio César Almeida Mendes
"""

from operacoesbd import *

conn = criarConexao("localhost", "root", "12345", "ouvidoria")
consulta = "SELECT * FROM manifestacoes"


def addManifestacao(conn):
    categorias = {
        "1": "Reclamação",
        "2": "Sugestão",
        "3": "Elogio",
        "4": "Denúncia",
        "5": "Outros"
    }

    print("Que tipo de manifestação deseja registrar?")
    for key, value in categorias.items():
        print(f"{key} - {value}")

    while True:
        categoria_opcao = input("Digite o número correspondente à categoria da manifestação: ")
        if categoria_opcao in categorias:
            categoria = categorias[categoria_opcao]
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    descricao = input("Digite a descrição da manifestação: ").strip()
    if not descricao:
        print("A descrição não pode estar vazia. Operação cancelada.")
        return

    query = "INSERT INTO manifestacoes (categoria, descricao) VALUES (%s, %s)"
    valores = (categoria, descricao)

    insertNoBancoDados(conn, query, valores)
    print("Manifestação registrada com sucesso!")
# addManifestacao(conn)
        

def listarManifestacoes(conn):
    consulta = "SELECT * FROM manifestacoes"
    manifestacoes = listarBancoDados(conn, consulta)
    
    if manifestacoes:
        for manifestacao in manifestacoes:
            print(f"\n ID: {manifestacao[0]} \n Tipo: {manifestacao[1]} \n Descrição: {manifestacao[2]}")
    else:
        print("Nenhuma manifestação encontrada.")
# listarManifestacoes(conn)

def excluirManifestacao(conn):
    id_manifestacao = int(input("Digite o ID da manifestação a ser excluída: ").strip())
    consulta_verificacao = "SELECT * FROM manifestacoes WHERE id = %s"
    dados_verificacao = (id_manifestacao,)
    manifestacao = listarBancoDados(conn, consulta_verificacao, dados_verificacao)

    if not manifestacao:
        print("Nenhuma manifestação encontrada com o ID fornecido. Operação cancelada.")
        return

    consulta = "DELETE FROM manifestacoes WHERE id = %s"
    dados = (id_manifestacao,)
    atualizarBancoDados(conn, consulta, dados)
    print("Manifestação excluída com sucesso!")
# excluirManifestacao(conn)

def pesquisarPorId(conn):
    id_manifestacao = int(input("Digite o ID da manifestação que deseja pesquisar: ").strip())
    consulta = "SELECT * FROM manifestacoes WHERE id = %s"
    dados = (id_manifestacao,)
    manifestacao = listarBancoDados(conn, consulta, dados)

    if manifestacao:
        for m in manifestacao:
            print(f"\n ID: {m[0]} \n Tipo: {m[1]} \n Descrição: {m[2]}")
    else:
        print("Nenhuma manifestação encontrada com o ID fornecido.")

def filtrarPorCategoria(conn):
    print("Escolha o tipo de manifestação para filtrar:")
    tipos = ["Reclamação", "Sugestão", "Elogio", "Denúncia", "Outros"]
    for i, tipo in enumerate(tipos, start=1):
        print(f"{i} - {tipo}")

    while True:
        tipo_opcao = input("Digite o número correspondente ao tipo: ").strip()
        if tipo_opcao.isdigit() and 1 <= int(tipo_opcao) <= len(tipos):
            tipo_escolhido = tipos[int(tipo_opcao) - 1]
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    consulta = "SELECT * FROM manifestacoes WHERE categoria = %s"
    dados = (tipo_escolhido,)
    manifestacoes = listarBancoDados(conn, consulta, dados)

    if manifestacoes:
        for manifestacao in manifestacoes:
            print(f"\n ID: {manifestacao[0]} \n Tipo: {manifestacao[1]} \n Descrição: {manifestacao[2]}")
    else:
        print(f"Nenhuma manifestação encontrada para o tipo '{tipo_escolhido}'.")

encerrarConexao(conn)