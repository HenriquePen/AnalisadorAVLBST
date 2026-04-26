# Ed2Apl22024 - Versão em Python

Este projeto é uma tradução do projeto Java original para Python, mantendo a mesma lógica geral de funcionamento.

## Estrutura

```text
Ed2Apl22024_python/
├── README.md
├── .gitignore
└── src/
    └── ed2apl22024/
        ├── avl_apl2_3.py
        ├── bst_apl2_3.py
        ├── supa_main_3.py
        └── __init__.py
```

## Arquivos principais

- `avl_apl2_3.py`: implementação da árvore AVL.
- `bst_apl2_3.py`: implementação da árvore BST.
- `supa_main_3.py`: menu principal do programa.

## Como executar

Entre na pasta do projeto e execute:

```bash
cd src/ed2apl22024
python supa_main_3.py
```

ou, dependendo da instalação:

```bash
python3 supa_main_3.py
```

## Observação sobre CSV

Assim como no código Java original, a opção de carregar CSV exige um caminho absoluto para o arquivo.

Exemplo no Windows:

```text
C:\Users\SeuUsuario\Downloads\arquivo.csv
```

Exemplo no Linux/WSL:

```text
/home/seuusuario/arquivo.csv
```

O CSV deve conter colunas com os nomes:

```text
COD_IBGE,VALOR_EXPORTACOES,LOCALIDADES,VALOR_IMPORTACOES
```

## Requisitos

Não é necessário instalar bibliotecas externas. O projeto usa apenas Python padrão.
