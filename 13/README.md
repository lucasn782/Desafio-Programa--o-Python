# Resolvedor de Sudoku (Backtracking)

## Descrição
Este exercício implementa um resolvedor de Sudoku 9x9 usando backtracking. Também inclui uma função para imprimir o tabuleiro de forma legível no terminal.

Arquivo principal: `sudoku.py`

## Funcionalidade
- `resolver_sudoku(sudoku)`: resolve o Sudoku substituindo zeros por números válidos
- `mostrar_sudoku(sudoku)`: imprime o tabuleiro com separadores de subgrades 3x3

## Algoritmo
1. Percorre as células em busca de um zero (vazio)
2. Tenta números de 1 a 9 verificando restrições de linha, coluna e subgrade 3x3
3. Se válido, recursivamente tenta resolver o restante
4. Se falhar, desfaz (backtrack) e tenta o próximo número
5. Retorna o tabuleiro resolvido ou `False` se não houver solução

## Código (núcleo da solução)
```python
from itertools import product

# ... resolver_sudoku(sudoku) e mostrar_sudoku(sudoku) ...
```

## Como Usar
- Edite a variável `sudoku` no final do arquivo com o puzzle desejado
- No Python interativo:
```bash
python -c "import sudoku as s; sol = s.resolver_sudoku([linha[:] for linha in s.sudoku]); s.mostrar_sudoku(sol)"
```

## Requisitos
- Python 3.x

## Observações
- `mostrar_sudoku` substitui zeros por `*` para destacar células vazias
- A função modifica a estrutura em lugar; crie uma cópia se quiser manter o original

## Melhorias Futuras
- Validação de entrada e detecção de puzzle inválido
- Heurísticas (MRV, forward checking) para acelerar a busca
- Interface CLI para carregar puzzles de arquivo