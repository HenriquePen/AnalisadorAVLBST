class NoAVL:
    def __init__(self, codIBGE, valorExportacoes, localidades, valorImportacoes):
        self.codIBGE = codIBGE
        self.valorExportacoes = valorExportacoes
        self.localidades = localidades
        self.valorImportacoes = valorImportacoes
        self.esquerda = None
        self.direita = None
        self.altura = 1


class AVL_Apl2_3:
    def __init__(self):
        self.raiz = None
        self.comparacoes = 0

    # Método para inserir um nó na árvore AVL
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
            return NoAVL(codIBGE, valorExportacoes, localidades, valorImportacoes)

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

        node.altura = 1 + max(self._altura(node.esquerda), self._altura(node.direita))
        return self._balancear(node)

    def _altura(self, node):
        return 0 if node is None else node.altura

    def _balancear(self, node):
        balance = self._altura(node.esquerda) - self._altura(node.direita)

        self.comparacoes += 1  # Comparação de balanceamento
        if (
            balance > 1
            and self._altura(node.esquerda.esquerda) >= self._altura(node.esquerda.direita)
        ):
            return self._rotacao_direita(node)

        self.comparacoes += 1  # Comparação de balanceamento
        if (
            balance < -1
            and self._altura(node.direita.direita) >= self._altura(node.direita.esquerda)
        ):
            return self._rotacao_esquerda(node)

        return node

    def _rotacao_direita(self, y):
        x = y.esquerda
        y.esquerda = x.direita
        x.direita = y
        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        x.direita = y.esquerda
        y.esquerda = x
        return y

    # Exibir árvore
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
