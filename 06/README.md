# Salvar e Carregar Dicionários com Pickle

## Descrição
Este exercício demonstra como serializar (salvar) e desserializar (carregar) dicionários Python em arquivos binários utilizando o módulo `pickle`.

Arquivos principais: `salvar_dicio.py`, `dicio.pickle` (exemplo de saída)

## Funcionalidade
- `salvar_dicio(dict_para_exportar, caminho_do_arquivo)`: salva o dicionário em um arquivo binário
- `carregar_dicio(caminho_do_arquivo)`: carrega e retorna o dicionário de um arquivo binário

## Código (núcleo da solução)
```python
import pickle

def salvar_dicio(dict_para_exportar, caminho_do_arquivo):
    with open(caminho_do_arquivo, 'wb') as arquivo:
        pickle.dump(dict_para_exportar, arquivo)
        
def carregar_dicio(caminho_do_arquivo):
    with open(caminho_do_arquivo, 'rb') as arquivo:
        return pickle.load(arquivo)
```

## Exemplos de Uso
```python
>>> from salvar_dicio import salvar_dicio, carregar_dicio
>>> dados = {"nome": "Ana", "idade": 30, "habilidades": ["python", "sql"]}
>>> salvar_dicio(dados, 'dados.pickle')
>>> restaurado = carregar_dicio('dados.pickle')
>>> restaurado
{'nome': 'Ana', 'idade': 30, 'habilidades': ['python', 'sql']}
```

## Como Usar
- Salvar:
```python
from salvar_dicio import salvar_dicio
salvar_dicio({"a": 1}, 'saida.pickle')
```
- Carregar:
```python
from salvar_dicio import carregar_dicio
d = carregar_dicio('saida.pickle')
print(d)
```

## Requisitos
- Python 3.x
- Módulo padrão `pickle`

## Observações
- Os arquivos gerados não são legíveis por humanos (binários)
- Não carregue arquivos pickle de fontes não confiáveis (pode executar código arbitrário)

## Melhorias Futuras
- Suporte a formatos mais portáveis (JSON/YAML) quando possível
- Validação de esquema dos dados antes de salvar/carregar