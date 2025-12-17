# Contagem de Palavras em um Arquivo de Texto

## Descrição
Este exercício lê um arquivo de texto e conta as ocorrências de cada palavra, exibindo o total de palavras e as 20 mais frequentes.

Arquivos principais: `palavras.py`, `artigo.txt` (arquivo de exemplo)

## Funcionalidade
A função `contar_palavras(caminho_do_arquivo)`:
- Lê o arquivo com codificação UTF-8
- Extrai palavras com regex `(\w+)`
- Converte tudo para maiúsculas
- Usa `collections.Counter` para contagem
- Exibe o total de palavras e as 20 mais comuns

## Código (núcleo da solução)
```python
import re
import collections

def contar_palavras(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'r', encoding='utf-8') as file:
        todas_palavras = re.findall(r"(\w+)", file.read())
        todas_palavras = [palavra.upper() for palavra in todas_palavras]
        print(f'\nNúmero total de palavras: {len(todas_palavras)}')
        contagem_palavras = collections.Counter(todas_palavras)
        print('\n20 palavras mais comuns:')
        for palavra in contagem_palavras.most_common(20):
            print(f'{palavra[0]}\t{palavra[1]}')
```

## Exemplos de Uso
```bash
python -c "from palavras import contar_palavras; contar_palavras('10/artigo.txt')"
```

## Requisitos
- Python 3.x

## Observações
- O padrão `\w` inclui letras, números e underscore, dependendo da localidade/Unicode
- Palavras são normalizadas para maiúsculas para contagem case-insensitive

## Melhorias Futuras
- Normalização Unicode/acento (NFKD) e remoção de pontuação
- Lista de stopwords e stemming/lematização
- Exportar resultados para CSV