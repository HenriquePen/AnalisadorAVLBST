import os
from dataclasses import dataclass

from avl_apl2_3 import AVL_Apl2_3
from bst_apl2_3 import BST_Apl2_3


@dataclass
class Resultado:
    codIBGE: int
    valor: float
    localidades: str

    def get_valor(self):
        return self.valor

    def get_codIBGE(self):
        return self.codIBGE

    def get_localidades(self):
        return self.localidades

    def __str__(self):
        return f"Cod_IBGE: {self.codIBGE}, Localidade: {self.localidades}, Diferença: {self.valor:.2f}"


def main():
    importacoesAVL = AVL_Apl2_3()
    exportacoesAVL = AVL_Apl2_3()
    importacoesBST = BST_Apl2_3()
    exportacoesBST = BST_Apl2_3()

    print("Escolha a estrutura de dados:")
    print("1 - Árvore BST")
    print("2 - Árvore AVL")
    escolha = get_input_int("Escolha uma opção (1 ou 2): ", 1, 2)

    if escolha == 1:
        executar_arvore(importacoesBST, exportacoesBST)
    else:
        executar_arvore(importacoesAVL, exportacoesAVL)


def executar_arvore(importacoes, exportacoes):
    while True:
        print("\nEscolha uma operação:")
        print("1 - Inserir")
        print("2 - Exibir Árvore")
        print("3 - Relatório de Crescimento/Declínio")
        print("4 - Relatório de Balança Comercial")
        print("5 - Inserir via CSV")
        print("6 - Sair")
        opcao = get_input_int("Escolha uma operação (1-6): ", 1, 6)

        if opcao == 1:
            inserir_dados(importacoes, exportacoes)
        elif opcao == 2:
            escolha = get_input_int(
                "Escolha a árvore para exibir (1 - Importações, 2 - Exportações): ",
                1,
                2,
            )
            if escolha == 1:
                exibir_arvore(importacoes)
            else:
                exibir_arvore(exportacoes)
        elif opcao == 3:
            gerar_relatorio_crescimento_declinio(importacoes, exportacoes)
        elif opcao == 4:
            gerar_relatorio_balanca_comercial(importacoes, exportacoes)
        elif opcao == 5:
            print("Insira o caminho do arquivo CSV:")
            caminho_arquivo = input().strip()
            carregar_dados_csv(importacoes, exportacoes, caminho_arquivo)
        elif opcao == 6:
            print("Programa encerrado.")
            return
        else:
            print("Opção inválida.")


def inserir_dados(importacoes, exportacoes):
    print("Insira Cod_IBGE, Valor Exportações, Localidades e Valor Importações:")
    codIBGE = get_input_int("Cod_IBGE: ", -2147483648, 2147483647)
    valorExportacoes = get_input_double("Valor Exportações: ")
    print("Localidades:")
    localidades = input()
    valorImportacoes = get_input_double("Valor Importações: ")

    tipo = get_input_int("Este valor é para: 1 - Importação ou 2 - Exportação? ", 1, 2)

    if tipo == 1:
        inserir_no(importacoes, codIBGE, 0, localidades, valorImportacoes)
    else:
        inserir_no(exportacoes, codIBGE, valorExportacoes, localidades, 0)


def exibir_arvore(arvore):
    if isinstance(arvore, (AVL_Apl2_3, BST_Apl2_3)):
        arvore.exibir_arvore()


def carregar_dados_csv(importacoes, exportacoes, caminho_arquivo):
    if not os.path.isabs(caminho_arquivo):
        print("Erro: O caminho fornecido não é absoluto.")
        return

    if not os.path.exists(caminho_arquivo):
        print("Erro: O arquivo não existe no caminho especificado!")
        return

    if os.path.isdir(caminho_arquivo):
        print("Erro: O caminho especificado é um diretório, não um arquivo!")
        return

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linha = arquivo.readline()
            if not linha:
                print("Erro: O arquivo CSV está vazio.")
                return

            delimiter = ","
            cabecalho = linha.rstrip("\n").split(delimiter)

            indiceIBGE = -1
            indiceLocalidades = -1
            indiceImportacao = -1
            indiceExportacao = -1

            for i, coluna_original in enumerate(cabecalho):
                coluna = coluna_original.strip().upper()
                if coluna == "COD_IBGE":
                    indiceIBGE = i
                elif coluna == "VALOR_EXPORTACOES":
                    indiceExportacao = i
                elif coluna == "LOCALIDADES":
                    indiceLocalidades = i
                elif coluna == "VALOR_IMPORTACOES":
                    indiceImportacao = i

            for linha in arquivo:
                linha = linha.rstrip("\n")
                try:
                    dados = linha.split(delimiter)

                    codIBGE = int(dados[indiceIBGE].strip())
                    localidades = dados[indiceLocalidades].strip()
                    valorImportacoes = float(dados[indiceImportacao].strip())
                    valorExportacoes = float(dados[indiceExportacao].strip())

                    if valorExportacoes > 0:
                        inserir_no(exportacoes, codIBGE, valorExportacoes, localidades, 0)
                    if valorImportacoes > 0:
                        inserir_no(importacoes, codIBGE, 0, localidades, valorImportacoes)
                except Exception:
                    print(f"Erro ao processar a linha: {linha}")

        print("Dados do CSV carregados com sucesso!")
    except Exception as erro:
        print("Erro ao ler o arquivo CSV. Verifique o caminho e o formato do arquivo.")
        print(erro)


def inserir_no(arvore, codIBGE, valorExportacoes, localidades, valorImportacoes):
    if isinstance(arvore, (AVL_Apl2_3, BST_Apl2_3)):
        arvore.inserir(codIBGE, valorExportacoes, localidades, valorImportacoes)


def gerar_relatorio_crescimento_declinio(importacoes, exportacoes):
    diferencas = calcular_diferencas(importacoes, exportacoes)
    diferencas.sort(key=lambda resultado: resultado.get_valor())
    print("\n5 Menores Diferenças:")
    for resultado in diferencas[:5]:
        print(resultado)


def gerar_relatorio_balanca_comercial(importacoes, exportacoes):
    diferencas = calcular_diferencas(importacoes, exportacoes)
    diferencas.sort(key=lambda resultado: resultado.get_valor(), reverse=True)
    print("\n5 Maiores Diferenças:")
    for resultado in diferencas[:5]:
        print(resultado)


def calcular_diferencas(importacoes, exportacoes):
    diferencas = []

    # Mantém a mesma lógica do código Java original:
    # o relatório percorre a árvore de importações recebida.
    if isinstance(importacoes, AVL_Apl2_3) and isinstance(exportacoes, AVL_Apl2_3):
        lista_importacoes = importacoes.get_lista_ordenada()
        for no in lista_importacoes:
            diferenca = no.valorExportacoes - no.valorImportacoes
            diferencas.append(Resultado(no.codIBGE, diferenca, no.localidades))
    elif isinstance(importacoes, BST_Apl2_3) and isinstance(exportacoes, BST_Apl2_3):
        lista_importacoes = importacoes.get_lista_ordenada()
        for no in lista_importacoes:
            diferenca = no.valorExportacoes - no.valorImportacoes
            diferencas.append(Resultado(no.codIBGE, diferenca, no.localidades))

    return diferencas


def get_input_int(message, min_value, max_value):
    while True:
        print(message, end="")
        try:
            entrada = int(input())
            if min_value <= entrada <= max_value:
                return entrada
            print("Erro: Entrada fora do intervalo permitido.")
        except Exception:
            print("Erro: Entrada inválida. Digite um número.")


def get_input_double(message):
    while True:
        print(message, end="")
        try:
            return float(input())
        except Exception:
            print("Erro: Entrada inválida. Digite um número decimal.")


if __name__ == "__main__":
    main()
