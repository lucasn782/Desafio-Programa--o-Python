# Jogo de Espera (Timing Game)

## Descrição
Este exercício cria um pequeno jogo de percepção de tempo. O objetivo é pressionar Enter novamente o mais próximo possível de um alvo aleatório entre 2 e 4 segundos.

Arquivo principal: `jogo_de_espera.py`

## Funcionalidade
A função `jogo_de_espera()`:
- Sorteia um objetivo de tempo aleatório entre 2 e 4 segundos
- Pede ao usuário para iniciar e depois para pressionar Enter novamente após o tempo alvo
- Mede o tempo decorrido com `time.perf_counter()` e informa a diferença

## Algoritmo
1. Gera um inteiro aleatório `objetivo ∈ [2, 4]`
2. Aguarda o primeiro Enter e registra `inicio`
3. Aguarda o segundo Enter e calcula `decorrido = perf_counter() - inicio`
4. Compara `decorrido` com `objetivo` e imprime o resultado

## Código (núcleo da solução)
```python
import time
import random

def jogo_de_espera():
    objetivo = random.randint(2, 4)
    print(f'\nSeu objetivo é de {objetivo} segundos')
    input(' ---Pressione Enter para começar--- ')
    inicio = time.perf_counter()
    input(f'\n...Pressione Enter de novo depois de {objetivo} segundos...')
    decorrido = time.perf_counter() - inicio
    print(f'\nTempo decorrido: {decorrido:.3f} segundos')
    if decorrido == objetivo:
        print('(Impressionante! Tempo perfeito!)')
    elif decorrido < objetivo:
        print(f'Eita! Rápido demais! Faltava ({objetivo - decorrido:.3f} segundos)')
    else:
        print(f'Iiii... Devagar demais... Sobrou ({decorrido - objetivo:.3f} segundos)')
```

## Como Usar
```bash
python jogo_de_espera.py
```

## Requisitos
- Python 3.x

## Observações
- Usa `time.perf_counter()` para alta precisão na medição
- A condição `decorrido == objetivo` raramente será verdadeira na prática devido à precisão temporal; considere tolerância se desejar.

## Melhorias Futuras
- Adicionar múltiplas rodadas e estatísticas
- Permitir configurar o intervalo do objetivo
- Implementar tolerância para considerar acertos aproximados