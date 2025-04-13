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
        "Opcão 1: Registrar Manifestação\n"
        "Opcão 2: Listar Manifestações\n"
        "Opcão 3: Excluir Manifestação\n"
        "Opcão 4: Sair"
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
        print("Sair")
        break

    else:
        print("Opção inválida")

encerrarConexao(conn)
