# Unir Arquivos CSV com Cabeçalhos Variáveis

## Descrição
Este exercício mescla múltiplos arquivos CSV em um único arquivo de saída, preservando todas as colunas encontradas (união de cabeçalhos) e escrevendo as linhas na sequência lida.

Arquivos principais: `unir_csv.py`, `alunos.csv`, `turma1.csv`, `turma2.csv`

## Funcionalidade
A função `unir_csv(arquivos, caminho_arquivo_resultante)`:
- Percorre a lista de arquivos para descobrir todos os campos (cabeçalhos)
- Escreve o cabeçalho unificado no CSV de saída
- Copia linha a linha dos arquivos de entrada para o arquivo de saída

## Código (núcleo da solução)
```python
import csv

def unir_csv(arquivos, caminho_arquivo_resultante):
    campos = []
    for arquivo in arquivos:
        with open(arquivo, 'r', encoding='utf-8') as csv_entrada:
            campo = csv.DictReader(csv_entrada).fieldnames
            campos.extend(f for f in campo if f not in campos)
            
    with open(caminho_arquivo_resultante, 'w', encoding='utf-8', newline='') as csv_saida:
        escrita = csv.DictWriter(csv_saida, fieldnames=campos)
        escrita.writeheader()
        for arquivo in arquivos:
            with open(arquivo, 'r', encoding='utf-8') as csv_entrada:
                leitor = csv.DictReader(csv_entrada)
                for linha in leitor:
                    escrita.writerow(linha)
```

## Exemplos de Uso
```python
>>> from unir_csv import unir_csv
>>> unir_csv(['12/alunos.csv', '12/turma1.csv', '12/turma2.csv'], '12/resultado.csv')
```

## Requisitos
- Python 3.x

## Observações
- Linhas com colunas faltantes terão células vazias para essas colunas no CSV resultante
- A ordem de colunas no resultado segue a primeira ocorrência de cada campo

## Melhorias Futuras
- Normalização de nomes de campos
- Opção para remover duplicatas
- Validação de tipos e dados