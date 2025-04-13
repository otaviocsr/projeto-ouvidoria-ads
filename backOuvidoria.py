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


encerrarConexao(conn)