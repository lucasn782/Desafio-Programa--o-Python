# Gerador de Senhas estilo Diceware

## Descrição
Este exercício implementa um gerador de senhas baseado no método Diceware, selecionando palavras aleatórias a partir de uma wordlist.

Arquivos principais: `gerador_de_senhas.py`, `diceware.wordlist.pt.txt`

## Funcionalidade
A função `gerar_senha(qtd_palavras, caminho_arquivo='diceware.wordlist.pt.txt')`:
- Lê uma wordlist (português) do arquivo indicado
- Ignora as 3 primeiras linhas (cabeçalho) e usa entradas até a linha 7778
- Extrai a segunda coluna (palavra) de cada linha
- Seleciona `qtd_palavras` termos pseudoaleatórios com `secrets.choice`
- Retorna a senha como uma string separada por espaços

## Código (núcleo da solução)
```python
import secrets

def gerar_senha(qtd_palavras, caminho_arquivo='diceware.wordlist.pt.txt'):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()[3:7779]
        lista_palavras = [line.split()[1] for line in linhas]
        
    palavras = [secrets.choice(lista_palavras) for i in range(qtd_palavras)]
    return ' '.join(palavras)
```

## Exemplos de Uso
```bash
python -c "from gerador_de_senhas import gerar_senha; print(gerar_senha(6))"
```

## Requisitos
- Python 3.x

## Observações
- Usa `secrets` para seleção criptograficamente segura
- Certifique-se de que o caminho para a wordlist está correto ao importar de outro diretório

## Melhorias Futuras
- Parâmetros para separador, capitalização e símbolos extras
- Métrica de entropia estimada
- Opção de usar diferentes wordlists