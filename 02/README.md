# Verificador de Palíndromos

## Descrição
Este exercício implementa uma função em Python para verificar se uma frase é um palíndromo, desconsiderando caracteres não alfabéticos e diferenças entre maiúsculas e minúsculas.

## Funcionalidade
A função `eh_palindromo(frase)`:
- Converte a frase para minúsculas
- Remove tudo que não for letra de a–z (ASCII)
- Compara a string resultante com sua versão invertida
- Retorna `True` se for palíndromo, caso contrário `False`

Arquivo principal: `palindromo.py`

## Algoritmo
1. Normaliza a entrada para minúsculas
2. Usa expressão regular para extrair somente letras `[a-z]+`
3. Junta os grupos em uma única string contínua
4. Inverte a string com slicing `[::-1]`
5. Compara as duas versões

## Código (núcleo da solução)
```python
import re

def eh_palindromo(frase):
    correta = ''.join(re.findall(r'[a-z]+', frase.lower()))
    revertida = correta[::-1]
    return correta == revertida
```

## Exemplos de Uso

### Palíndromo simples
```python
>>> eh_palindromo("arara")
True
```

### Frase com pontuação e espaços
```python
>>> eh_palindromo("Socorram-me, subi no onibus em Marrocos!")
True
```

### Não-palíndromo
```python
>>> eh_palindromo("Olá mundo!")
False
```

Observação: o regex atual (`[a-z]`) considera apenas letras ASCII sem acentos. Frases com acentos terão os acentos removidos (ex.: "ônibus" -> "onibus").

## Como Usar
1. Salve o arquivo `palindromo.py`
2. Importe e chame a função no seu código Python:
   ```python
   from palindromo import eh_palindromo
   print(eh_palindromo("Socorram-me, subi no onibus em Marrocos!"))
   ```
3. Ou execute direto no terminal:
   ```bash
   python -c "from palindromo import eh_palindromo; print(eh_palindromo('arara'))"
   ```

## Requisitos
- Python 3.x
- Módulo padrão `re` (expressões regulares)

## Aplicações
- Validação de strings
- Exercícios de manipulação de textos
- Demonstração de uso de expressões regulares e slicing em Python

## Observações
- A comparação é case-insensitive
- Caracteres não alfabéticos são ignorados
- Para suporte completo a acentos/Unicode, adapte o regex para incluir letras acentuadas (por exemplo usando `\w` com normalização Unicode) ou utilize normalização (`unicodedata.normalize`).

## Melhorias Futuras
- Normalização Unicode para manter letras com acento corretamente
- Opção para ignorar/considerar números
- Versão que retorna também a string normalizada usada na comparação