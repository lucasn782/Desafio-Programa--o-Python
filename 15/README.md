# Baixar Arquivos Sequenciais

## Descrição
Este projeto contém uma função Python para baixar arquivos sequenciais de uma URL base. A função identifica um padrão numérico na URL e tenta baixar arquivos subsequentes até encontrar erros consecutivos, útil para baixar séries de imagens ou arquivos numerados.

## Funcionalidade
A função `baixar_arquivos(primeira_url, output_dir)` recebe uma URL inicial e um diretório de saída. Ela analisa a URL para encontrar o último número no caminho, cria o diretório se necessário, e baixa arquivos incrementando o número até que ocorram 3 erros consecutivos de download.

## Algoritmo
O algoritmo funciona da seguinte maneira:
1. Verifica se o diretório de saída existe; se não, cria-o
2. Divide a URL em componentes usando `urlsplit`
3. Extrai o último número do caminho da URL usando regex
4. Inicializa contador e contador de erros
5. Em um loop, incrementa o número e constrói a nova URL
6. Tenta baixar o arquivo; se sucesso, imprime mensagem; se erro, incrementa contador de erros
7. Para quando erros atingem 3

## Código
```python
import os
import re
from urllib.parse import urlsplit, urlunsplit
from urllib.request import urlretrieve

def baixar_arquivos(primeira_url, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    protocolo, dominio, caminho, filtro, fragmento = urlsplit(primeira_url)
    atual = re.findall(r'[0-9]+', caminho)[-1]

    contador, erros = 0, 0
    while erros < 3:
        proximo = str(int(atual) + contador)
        if atual[0] == '0':  
            proximo = '0' * (len(atual) - len(proximo)) + proximo
        novo_caminho = caminho.replace(atual, proximo)
        proxima_url = urlunsplit([protocolo, dominio, novo_caminho, filtro, fragmento])
        try:
            arquivo_destino = os.path.join(output_dir, os.path.basename(proxima_url))
            urlretrieve(proxima_url, arquivo_destino)
            print(f'Arquivo {os.path.basename(proxima_url)} baixado com sucesso de {proxima_url}')
        except IOError:
            print(f'Não foi possivel encontrar {proxima_url}')
            erros += 1
        contador += 1
```

## Exemplos de Uso

### Exemplo 1: Baixar imagens sequenciais
```python
>>> url = 'https://jtemporal.com/images/gitfichas/001.jpg'
>>> baixar_arquivos(url, 'imagens')
Arquivo 001.jpg baixado com sucesso de https://jtemporal.com/images/gitfichas/001.jpg
Arquivo 002.jpg baixado com sucesso de https://jtemporal.com/images/gitfichas/002.jpg
...
```
Este exemplo baixa imagens numeradas de 001.jpg em diante até que não haja mais arquivos disponíveis.

### Exemplo 2: Com zeros à esquerda
Se a URL inicial tiver zeros à esquerda no número, a função preserva o formato:
```python
>>> url = 'https://example.com/files/0001.txt'
>>> baixar_arquivos(url, 'downloads')
```
Baixará 0001.txt, 0002.txt, etc., mantendo os zeros à esquerda.