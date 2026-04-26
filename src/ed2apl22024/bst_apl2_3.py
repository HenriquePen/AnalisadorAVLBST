class NoBST:
    def __init__(self, codIBGE, valorExportacoes, localidades, valorImportacoes):
        self.codIBGE = codIBGE
        self.valorExportacoes = valorExportacoes
        self.localidades = localidades
        self.valorImportacoes = valorImportacoes
        self.esquerda = None
        self.direita = None


class BST_Apl2_3:
    def __init__(self):
        self.raiz = None
        self.comparacoes = 0

    # Método para inserir um nó na árvore BST
    def inserir(self, codIBGE, valorExportacoes, localidades, valorImportacoes):
        self.raiz = self._inserir_rec(
            self.raiz,
            codIBGE,
            valorExportacoes,
            localidades,
            valorImportacoes,
        )

    def _inserir_rec(self, node, codIBGE, valorExportacoes, localidades, valorImportacoes):
        self.comparacoes += 1  # Comparação para verificação de nulo
        if node is None:
            return NoBST(codIBGE, valorExportacoes, localidades, valorImportacoes)

        self.comparacoes += 1  # Comparação para decidir a direção
        if codIBGE < node.codIBGE:
            node.esquerda = self._inserir_rec(
                node.esquerda,
                codIBGE,
                valorExportacoes,
                localidades,
                valorImportacoes,
            )
        elif codIBGE > node.codIBGE:
            node.direita = self._inserir_rec(
                node.direita,
                codIBGE,
                valorExportacoes,
                localidades,
                valorImportacoes,
            )

        return node

    # Exibir a árvore
    def exibir_arvore(self):
        print("Diagrama da Árvore:")
        self._print_tree(self.raiz, "", False)
        print(f"Total de comparações: {self.comparacoes}")

    def _print_tree(self, node, prefix, is_left):
        if node is not None:
            ramo = "├── " if is_left else "└── "
            print(
                f"{prefix}{ramo}Cod_IBGE: {node.codIBGE}, "
                f"Localidade: {node.localidades}, "
                f"Importações: {node.valorImportacoes}, "
                f"Exportações: {node.valorExportacoes}"
            )
            novo_prefixo = prefix + ("│   " if is_left else "    ")
            self._print_tree(node.esquerda, novo_prefixo, True)
            self._print_tree(node.direita, novo_prefixo, False)

    # Método para buscar um nó por codIBGE
    def buscar(self, codIBGE):
        return self._buscar_rec(self.raiz, codIBGE)

    def _buscar_rec(self, node, codIBGE):
        if node is None or node.codIBGE == codIBGE:
            return node
        if codIBGE < node.codIBGE:
            return self._buscar_rec(node.esquerda, codIBGE)
        return self._buscar_rec(node.direita, codIBGE)

    # Método para obter a raiz da árvore
    def get_raiz(self):
        return self.raiz

    # Método para obter uma lista ordenada de todos os nós (In-order Traversal)
    def get_lista_ordenada(self):
        lista = []
        self._in_order_traversal(self.raiz, lista)
        return lista

    def _in_order_traversal(self, node, lista):
        if node is not None:
            self._in_order_traversal(node.esquerda, lista)
            lista.append(node)
            self._in_order_traversal(node.direita, lista)
