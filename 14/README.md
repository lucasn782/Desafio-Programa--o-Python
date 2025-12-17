# Compactador de Arquivos por Extensão (ZIP)

## Descrição
Este exercício cria um arquivo ZIP contendo apenas os arquivos de determinadas extensões encontrados recursivamente dentro de uma pasta.

Arquivos principais: `cria_zip.py`, pasta de exemplo `para_compactar/` e `minhas-fotos.zip`

## Funcionalidade
`compactar(pasta, lista_extensoes, caminho_resultado)`:
- Percorre a pasta com `os.walk`
- Seleciona arquivos cuja extensão esteja em `lista_extensoes` (case-insensitive)
- Adiciona-os ao ZIP preservando o caminho relativo à pasta base

## Código (núcleo da solução)
```python
import os
from zipfile import ZipFile

def compactar(pasta, lista_extensoes, caminho_resultado):
    with ZipFile(caminho_resultado, 'w') as zip_resultante:
        for raiz, _, arquivos in os.walk(pasta):
            caminho_relativo = os.path.relpath(raiz, pasta)
            for arquivo in arquivos:
                _, ext = os.path.splitext(arquivo)
                if ext.lower() in lista_extensoes:
                    zip_resultante.write(
                        os.path.join(raiz, arquivo),
                        arcname=os.path.join(caminho_relativo, arquivo)
                    )
```

## Exemplos de Uso
```python
>>> from cria_zip import compactar
>>> compactar('14/para_compactar', ['.jpg', '.png'], '14/minhas-fotos.zip')
```

## Requisitos
- Python 3.x

## Observações
- `lista_extensoes` deve conter o ponto, por exemplo: `['.jpg', '.png']`
- Arquivos já contidos no ZIP de exemplo são resultado de execução prévia

## Melhorias Futuras
- Opção para compactação com níveis (ZIP_DEFLATED)
- Excluir diretórios/arquivos por padrões (glob/regex)
- CLI para passar argumentos via linha de comando