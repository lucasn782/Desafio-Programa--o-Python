# Probabilidade de Resultados com Dados

## Descrição
Este exercício simula lançamentos de dados e calcula a probabilidade de cada soma possível, exibindo os resultados em porcentagem.

Arquivo principal: `probabilidade_dados.py`

## Funcionalidade
A função `simular_dados(*dados, tentativas=1_000_000)`:
- Recebe os números de lados dos dados (ex.: `6, 6` para 2D6)
- Realiza `tentativas` simulações e contabiliza as somas
- Exibe a distribuição de probabilidades de cada soma possível

## Código (núcleo da solução)
```python
from random import randint
from collections import Counter

def simular_dados(*dados, tentativas=1_000_000):
    contagens = Counter()
    for _ in range(tentativas):
        contagens[sum((randint(1, lados) for lados in dados))] += 1
        
    print('\nPROBABILIDADE DE RESULTADOS')
    for resultado in range(len(dados), sum(dados) + 1):
        print(f'{resultado}\t{contagens[resultado] * 100 / tentativas :0.2f}%')
```

## Exemplos de Uso
```bash
python -c "from probabilidade_dados import simular_dados; simular_dados(6, 6, tentativas=100000)"
```

## Requisitos
- Python 3.x

## Observações
- O tempo de execução cresce com `tentativas`; ajuste conforme necessidade
- Os resultados convergem para as probabilidades teóricas conforme `tentativas` aumenta

## Melhorias Futuras
- Plotar histograma com `matplotlib`
- Retornar os dados em vez de imprimir (para análise programática)
- Suporte a sementes para reprodutibilidade (`random.seed`)