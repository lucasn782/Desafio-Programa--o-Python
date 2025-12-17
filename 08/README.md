# Jogo da Forca (Terminal)

## Descrição
Este exercício implementa uma versão simples do jogo da forca jogado no terminal. O jogo escolhe aleatoriamente um tema e uma palavra, e o usuário tenta adivinhar letra a letra dentro de um número limitado de tentativas.

Arquivo principal: `forca.py`

## Funcionalidade
- Seleção aleatória de tema e palavra (`curso`, `frutas`, `paises`, `animais`)
- Exibição do tabuleiro com letras descobertas e tentativas restantes
- Loop de jogo que aceita chutes de letras e verifica vitória ou derrota

## Código (núcleo da solução)
```python
import os
import random

# ... escolher_palavra(), mostrar_tabuleiro(), jogo_da_forca() ...
```

## Como Usar
```bash
python -c "from forca import jogo_da_forca; jogo_da_forca()"
```

## Requisitos
- Python 3.x

## Observações
- A limpeza da tela usa `os.system('clear' if posix else 'cls')`
- `tentativas = len(palavra) - 1` define a dificuldade com base no tamanho da palavra
- Não há validações para múltiplas letras por chute; entradas são convertidas para minúsculas

## Melhorias Futuras
- Evitar descontar tentativa em chutes repetidos
- Mostrar letras incorretas já tentadas
- Adicionar arte ASCII da forca
- Suporte a acentos e normalização de entrada