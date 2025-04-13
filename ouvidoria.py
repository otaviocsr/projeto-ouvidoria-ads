"""
    Sistema de Ouvidoria 
    Autor: Otávio César Almeida Mendes
"""

from operacoesbd import *
from backOuvidoria import *

conn = criarConexao("localhost", "root", "12345", "ouvidoria")
consulta = "SELECT * FROM manifestacoes"

opcao = 0

while True:
    print("=" * 35)
    print(  
        "Opcão 1: Registrar manifestação\n"
        "Opcão 2: Listar todas as manifestações\n"
        "Opcão 3: Excluir manifestação\n"
        "Opção 4: Pesquisar por ID\n"
        "Opção 5: Pesquisar por Categoria\n"
        "Opção 6: Sair"
        )
    print("=" * 35)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        addManifestacao(conn)

    elif opcao == 2: 
        listarManifestacoes(conn)

    elif opcao == 3:
        excluirManifestacao(conn)

    elif opcao == 4:
        pesquisarPorId(conn)
        
    elif opcao == 5:
        filtrarPorCategoria(conn)

    elif opcao == 6:
        print("Sair")
        break

    else:
        print("Opção inválida")

encerrarConexao(conn)
