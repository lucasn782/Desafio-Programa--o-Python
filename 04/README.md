# Encontrando Índices em Listas Aninhadas

## Descrição
Este exercício implementa uma função para localizar todas as ocorrências de um item dentro de uma lista que pode conter sublistas (aninhadas). O resultado retorna os caminhos de índices (como listas de índices) até cada ocorrência encontrada.

Arquivo principal: `encontrando_indices.py`

## Funcionalidade
A função `encontre_indices(lista, item)`:
- Percorre a lista recursivamente
- Para cada ocorrência igual a `item`, retorna o caminho dos índices até ela
- Em sublistas, concatena o índice atual ao caminho retornado pela recursão
- Retorna uma lista de caminhos (cada caminho é uma lista de índices)

## Algoritmo
1. Inicializa uma lista vazia para armazenar os caminhos
2. Itera com `enumerate` sobre os elementos
3. Se o elemento for igual ao `item`, adiciona `[indice]`
4. Se o elemento for uma lista, chama recursivamente e concatena o índice atual com cada caminho retornado
5. Retorna a lista de caminhos

## Código (núcleo da solução)
```python
def encontre_indices(lista, item):
    lista_de_indices = []
    for indice, value in enumerate(lista):
        if value == item:
            lista_de_indices.append([indice])
        elif isinstance(lista[indice], list):
            for i in encontre_indices(lista[indice], item):
                lista_de_indices.append([indice] + i)
    return lista_de_indices
```

## Exemplos de Uso
```python
>>> from encontrando_indices import encontre_indices
>>> dados = [1, [2, 3, [1, 2]], 4, [1, [2, 1]]]
>>> encontre_indices(dados, 1)
[[0], [1, 2, 0], [3, 0], [3, 1, 1]]

>>> encontre_indices(dados, 2)
[[1, 0], [1, 2, 1], [3, 1, 0]]
```

## Como Usar
- Modo interativo:
```bash
python -c "from encontrando_indices import encontre_indices; print(encontre_indices([1,[2,3,[1,2]],4,[1,[2,1]]], 1))"
```

## Requisitos
- Python 3.x

## Observações
- A função trata arbitrariamente níveis de aninhamento
- O retorno é uma lista possivelmente vazia caso o `item` não seja encontrado

## Melhorias Futuras
- Suporte a outras coleções (tuplas, dicionários)
- Parâmetro para limitar profundidade de busca
- Opção de retornar gerador para streams grandes